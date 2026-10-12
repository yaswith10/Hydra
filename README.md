# Hydra

**AI-powered incident investigation and recovery platform.**

Hydra aims to investigate application failures, identify root causes, and support safe, verified recovery through observability data and AI-assisted analysis.

## Table of Contents

* [Overview](#overview)
* [Architecture](#architecture)
* [Tech Stack](#tech-stack)
* [Implementation Status](#implementation-status)
* [Getting Started](#getting-started)

## Overview

Hydra is being developed to investigate and respond to failures in distributed applications. It will combine telemetry, diagnostic workflows, and AI-assisted reasoning to help identify incidents and evaluate recovery actions.

## Architecture

Hydra consists of two main parts:

* **Hydra Platform:** The control plane responsible for incident investigation and recovery workflows.
* **Reference E-Commerce Application:** A set of independently running services used to simulate real-world application behavior and failures.

## Tech Stack

* **Backend:** Python, Django, Django REST Framework
* **Database:** PostgreSQL
* **Containerization:** Docker, Docker Compose
* **Observability:** OpenTelemetry, Prometheus, Grafana *(planned)*
* **AI-assisted investigation:** LLM-based workflows *(planned)*

## Implementation Status

* [x] Initial project structure
* [x] Initial reference application service
* [x] PostgreSQL persistence
* [x] Basic order lifecycle and API endpoints
* [x] Initial automated tests
* [x] Dockerized reference application and PostgreSQL
* [x] Automated database migrations during application startup
* [x] Basic application health endpoint
* [ ] Structured logging and distributed tracing
* [ ] Metrics collection and dashboards
* [ ] Incident detection and investigation workflows
* [ ] AI-assisted root cause analysis
* [ ] Safe remediation and recovery verification
* [ ] Fault injection and evaluation framework

## Getting Started

### Prerequisites

Install the following software:

* [Git](https://git-scm.com/)
* [Docker Engine](https://docs.docker.com/engine/install/)
* [Docker Compose](https://docs.docker.com/compose/install/)

### 1. Clone the Repository

```bash
git clone <repository-url>
cd Hydra/reference-ecommerce
```

Replace `<repository-url>` with the URL of the Hydra Git repository.

### 2. Configure Environment Variables

Create `order-service/.env` and add:

```dotenv
POSTGRESQL_NAME=hydra_orders
POSTGRESQL_USER=hydra
POSTGRESQL_PASSWORD=replace_with_a_secure_password
POSTGRESQL_HOST=localhost
POSTGRESQL_PORT=5432

DJANGO_SECRET_KEY=replace_with_a_secret_key
DEBUG=True
```

Use secure, unique values for the database password and Django secret key. Never commit `.env` to version control.

When running through Docker Compose, the Order Service must use `POSTGRESQL_HOST=db`. The Compose configuration should override this value inside the container; `localhost` is for running Django directly on the host.

Ensure the Compose configuration uses the same `POSTGRESQL_*` variable names and passes the database credentials to PostgreSQL and the Order Service.

### 3. Start the Application

From the `reference-ecommerce/` directory, make `POSTGRESQL_PASSWORD` and `DJANGO_SECRET_KEY` available to Docker Compose. Then run:

```bash
docker compose up --build -d
```

The Order Service applies pending database migrations during startup.

### 4. Verify the Setup

Check the container status:

```bash
docker compose ps
```

Check the health endpoint:

```bash
curl http://localhost:8000/health/
```

Expected response:

```json
{"status": "ok"}
```

View application logs:

```bash
docker compose logs -f order-service
```

### 5. Stop the Application

```bash
docker compose down
```

This stops and removes the containers while preserving the PostgreSQL named volume and its data.

**Warning:** Running `docker compose down -v` also removes the database volume and deletes its stored data.

For component-specific instructions, see the README files within the relevant directories.
