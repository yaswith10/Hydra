# Changelog

Notable changes to the Hydra project are documented here.

## [Unreleased]

### Added

* Implemented the initial Order Service using Django REST Framework.
* Added order creation and retrieval APIs.
* Added order lifecycle transitions: `PENDING`, `INVENTORY_RESERVED`, `PAYMENT_COMPLETED`, and `COMPLETED`.
* Added a basic application health endpoint.
* Configured PostgreSQL persistence for the Order Service.
* Added initial tests for order creation, validation, retrieval, and lifecycle transition rules.

### Changed

* Replaced SQLite with PostgreSQL for local Order Service development.

### Known limitations

* Inventory and payment operations are currently simulated.
* Structured application logging and distributed tracing are not yet implemented.
