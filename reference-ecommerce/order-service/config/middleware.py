import uuid
import time
import logging
from django.conf import settings
from django.http import HttpResponseBadRequest, HttpResponseServerError

from .logging_context import request_id_var


logger = logging.getLogger(__name__)

class RequestIDMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request_id = uuid.uuid4()
        request.request_id = request_id

        token = request_id_var.set(request_id)
        request_start_time = time.perf_counter()
        try:
            response = self.get_response(request)
            request_duration = (time.perf_counter() - request_start_time)
            logger.info(
                "HTTP request completed: method=%s, path=%s, status=%s, duration_ms=%.2f",
                request.method,
                request.path,
                response.status_code,
                request_duration
            )
            response["X-Request-ID"] = request_id
            return response
        finally:
            request_id_var.reset(token)

class FaultInjectionMiddleware:

    MAX_DELAY_SECONDS = 5

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # code exectued before request
        delay_header = request.headers.get("X-Hydra-Inject-Delay")
        error_header = request.headers.get("X-Hydra-Inject-Error")

        if delay_header is None and error_header is None:
            return self.get_response(request)

        if not settings.DEBUG:
            return HttpResponseBadRequest(
                "Fault injection is disabled in production"
            )

        if error_header:
            try:
                error = int(error_header)
            except ValueError:
                return HttpResponseBadRequest(
                    "Error status code for deliberate fault injection should be should be 500"
                )
            if error != 500:
                return HttpResponseBadRequest(
                    "Error status code for deliberate fault injection should be should be 500"
                )
            return HttpResponseServerError(
                "Deliberately injected fault error by Hydra"
            )
        try:
            delay = float(delay_header)
        except ValueError:
            return HttpResponseBadRequest(
                f"The Delay must be at most the {self.MAX_DELAY_SECONDS} seconds and greater that 0 seconds"
            )
        if delay <= 0 or delay > self.MAX_DELAY_SECONDS: 
            return HttpResponseBadRequest(
                f"The Delay must be at most the {self.MAX_DELAY_SECONDS} seconds and greater that 0 seconds"
            )

        time.sleep(delay)

        response = self.get_response(request)

        # code executed after request
        return response

