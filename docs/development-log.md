# Hydra Development Log

This document records Hydra's day-to-day engineering progress, implementation decisions, debugging work, and planned improvements. Entries are organized by development date.

## 21-10-2026
* Started making deliberate fault injections. Today we have created and added FaultInjectionMiddleware which induces delay from the request header X-Hydra-Inject-Delay.
* After that we have added deliberated error injection using header X-Hydra-Inject-Error in the same FaultInjectionMiddleware.
* Now deliberate fault injection step is completed. Now lets start core Hydra which finds these deliberate errors.
* In Hydra Observer application, we have created the integratons app to integrate a reference application to our hydra observer.
* Created Application model. It represents reference application.

## 18-10-2026
* Configured Grafana with Prometheus as its data source and created three monitoring panels for HTTP request rate, response status, and request latency.
* Here by, the basic setup of refernce-application is completed. From next week, Controlled Incident Simulation phase will begin

## 15-10-2026
* Integrated django-prometheus into order service to expose application metrics at /metrics.
* Added prometheus to docker compose and configured to scrape the order service every 5 seconds.
* Resolved Docker port mapping and django ALLOWED_HOSTS configuration issues to establish sucessful metric collection.
* verified prometheus target is UP and collecting metrics from Order Service.

## 12-10-2026

* Added and Configured Opentelemetry to observe the requests.

## 11-10-2026

* Added Logging functionality to the order-service using python-json-logger.
* Added middleware to generate and store random request-id.
* Added Logging for each request.
* Configured docker and Update the README.md to start the application.

## 10-10-2026

* Added order amount validation, retrieval APIs, and initial automated tests.
* Implemented order lifecycle transitions and inventory, payment, and completion endpoints.
* Configured PostgreSQL persistence and fixed environment-related issues.
* Added a basic application health endpoint.

## 09-10-2026

* Implemented the Order model and initial database migration.
* Created DRF serializers and list/create order API endpoints.
* Configured URL routing for the Order Service.

## 08-10-2026

* Initialized the Hydra repository and Django Order Service project.
* Created the `orders` Django application.
* Configured environment variables and `.env.example`.
* Hydra -> Reference-Ecommerce -> Order-Service. Currently workiong on order-service
