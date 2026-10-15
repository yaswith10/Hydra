# Hydra Development Log

This document records Hydra's day-to-day engineering progress, implementation decisions, debugging work, and planned improvements. Entries are organized by development date and reconstructed from Git history and project notes.

## 15-10-2026


## 12-10-2026

* Added and Configured Opentelemetry to observe the requests

## 11-10-2026

* Added Logging functionality to the order-service using python-json-logger
* Added middleware to generate and store random request-id
* Added Logging for each request
* Configured docker and Update the README.md to start the application

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
