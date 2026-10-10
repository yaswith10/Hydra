# Hydra

**AI-powered incident investigation and recovery platform.**

Hydra aims to help investigate application failures, identify root causes, and support safe, verified recovery through observability data and AI-assisted analysis.

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
* **Observability:** OpenTelemetry, Prometheus, Grafana *(planned)*
* **AI-assisted investigation:** LLM-based workflows *(planned)*

## Implementation Status

* [x] Initial project structure
* [x] Initial reference application service
* [x] PostgreSQL persistence
* [x] Basic order lifecycle and API endpoints
* [x] Initial automated tests
* [ ] Structured logging and distributed tracing
* [ ] Metrics collection and dashboards
* [ ] Incident detection and investigation workflows
* [ ] AI-assisted root cause analysis
* [ ] Safe remediation and recovery verification
* [ ] Fault injection and evaluation framework

## Getting Started

The project is under active development. Individual components have their own setup instructions.

Start with the [Reference E-Commerce Application](reference-ecommerce/) to explore the workload used to develop and test Hydra.
