import uuid
import time
import logging

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
