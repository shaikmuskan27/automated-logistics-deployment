# 🚚 Automated Logistics Deployment Pipeline

[![CI/CD Pipeline](https://github.com/shaikmuskan27/automated-logistics-deployment/actions/workflows/deploy.yml/badge.svg)](https://github.com/shaikmuskan27/automated-logistics-deployment/actions/workflows/deploy.yml)

## 🌟 Project Overview
This project demonstrates a high-availability CI/CD pipeline designed for a containerized logistics application. It focuses on **Infrastructure as Code (IaC)**, **DevSecOps**, and **Automated Health Monitoring**.

### 🛠 Key Features
* **Containerization:** Packaged using Docker for 100% environment consistency.
* **DevSecOps Gate:** Integrated `Trivy` scanning to block any build with `CRITICAL` or `HIGH` vulnerabilities.
* **Resilient Health Checks:** Automated connectivity testing using `curl` with built-in retries to ensure system stability post-deployment.
* **Automated Workflow:** GitHub Actions orchestrates the entire lifecycle from commit to verification.

## 🛡️ Security Audit Results
Current status: **0 Vulnerabilities Detected.**

| Target | Type | Vulnerabilities | Status |
| :--- | :--- | :--- | :--- |
| logistics-app (Debian) | OS | 0 | ✅ SECURE |
| Python Packages (Flask) | Language | 0 | ✅ SECURE |

---
*Built for the Systems Development Engineer (SysDE) Career Path.*

## 📸 Project Evidence

### CI/CD Pipeline Success
![Pipeline Success](Screenshot 2026-01-06 111820.png)

### Security Scan Results (0 Vulnerabilities)
![Security Report](Screenshot 2026-01-06 111222.png)