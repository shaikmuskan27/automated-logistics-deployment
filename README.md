[![CI/CD Pipeline](https://github.com/shaikmuskan27/automated-logistics-deployment/actions/workflows/deploy.yml/badge.svg)](https://github.com/shaikmuskan27/automated-logistics-deployment/actions/workflows/deploy.yml)# Automated Logistics Deployment Pipeline
An automated CI/CD pipeline built to simulate "Last Mile" logistics monitoring, ensuring consistent infrastructure deployment via containerization.

## 🛠 Tech Stack
* **Language:** Python (Flask API)
* **Infrastructure:** Docker (Containerization)
* **Automation:** GitHub Actions (CI/CD Pipeline)
* **Environment:** Windows (WSL2) / Linux (Ubuntu-latest)

## 🚀 Features
* **Automated Build:** Every code push triggers a Docker build to ensure environment consistency.
* **Health Check Testing:** The pipeline includes a connectivity test that validates the web server's response before completing the deployment.
* **Conflict Resolution:** Managed complex Git versioning issues using rebase and force-syncing strategies.

## 📈 SysDE Skills Demonstrated
* Infrastructure as Code (Dockerfile)
* CI/CD Workflow Orchestration (YAML)
* Linux Command Line Proficiency
* Version Control Best Practices (Git)