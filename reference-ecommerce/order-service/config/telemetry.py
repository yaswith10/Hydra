import os

from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.instrumentation.django import DjangoInstrumentor

def configure_tracing():
    if trace.get_tracer_provider().__class__.__name__ != "ProxyTracerProvider":
        return

    resource = Resource.create({
        "service.name" : os.getenv(
            "OTEL_SERVICE_NAME",
            "hydra-order-service"
        )
    })

    provider = TracerProvider(resource=resource)

    exporter = OTLPSpanExporter(
        endpoint=os.getenv(
            "OTEL_EXPORTER_OTLP_TRACES_ENDPOINT",
            "http://jaeger:4318/v1/traces"
        )
    )

    provider.add_span_processor(BatchSpanProcessor(exporter))
    trace.set_tracer_provider(provider)
    DjangoInstrumentor().instrument()