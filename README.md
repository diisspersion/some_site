# System Resource Monitor

A lightweight web application built with **FastAPI** to monitor system resources in real-time. This project is designed as a sandbox for practicing Python scripting, Dockerization, and CI/CD pipeline configuration.

---

## 🚀 Features

* **Web Dashboard:** Visualize CPU, RAM, and Disk usage via a Jinja2-powered frontend.
* **System Metrics:** Real-time data fetching using the `psutil` library.
* **Authentication:** Basic login mechanism to protect sensitive data.
* **Docker Ready:** Easily containerized for consistent deployment.

---

## 🛠 Tech Stack

* **Backend:** FastAPI (Python 3.10+)
* **Templates:** Jinja2 + HTML/CSS
* **System Monitoring:** psutil
* **Deployment:** Docker & Docker Compose

---

## ⚙️ Environment Variables

The application uses environment variables for configuration. You can set these in your shell or a `.env` file:

| Variable | Description | Default Value |
| --- | --- | --- |
| `ADMIN_USERNAME` | Username for dashboard access | `admin` |
| `ADMIN_PASSWORD` | Password for dashboard access | `admin123` |
| `API_TOKEN` | Secret token for API interactions | `fallback-token` |

---

## 🧪 CI/CD Goals

This project is used to practice:

* Writing **GitHub Actions** or **GitLab CI** workflows.
* Automated linting with `flake8` or `black`.
* Building and pushing Docker images to **Docker Hub** or **GHCR**.
* Deploying to a staging/production server.

---
