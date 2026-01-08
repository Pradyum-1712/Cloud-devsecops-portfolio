🛡️ SecureCloud-Ops: Automated DevSecOps Pipeline & Dashboard

📋 Project Overview

In modern cloud environments, security cannot be an afterthought. This project demonstrates a "Shift-Left" DevSecOps methodology, where security auditing is integrated directly into the development lifecycle. I architected an automated CI/CD pipeline that builds, secures, and prepares a containerized application for deployment to Microsoft Azure.

The core of the project is a Security Gate that prevents vulnerable code from ever reaching production, coupled with a Hardened Container strategy to minimize the attack surface.

🚀 Key Features

Infrastructure as Code (IaC): Used Terraform to define immutable Azure cloud resources (Resource Groups, App Service Plans, and Web Apps).

Automated Security Gate: Integrated Trivy into GitHub Actions to perform deep scans of container images. The pipeline is configured to fail automatically if CRITICAL or HIGH vulnerabilities are detected.

Container Hardening: Re-engineered the application to run on Python 3.12-Alpine Linux, significantly reducing the image size and eliminating unnecessary packages that increase security risk.

Visual Security Interface: Developed a Flask-based Security Dashboard using Tailwind CSS to visualize system health, container metadata, and audit logs.

Configuration Management: Implemented professional .gitignore standards to prevent the leakage of sensitive cloud credentials and system junk files.

🛠️ Technology Stack

Category

Tools & Technologies

Cloud Platform

Microsoft Azure (App Services, Resource Groups)

Infrastructure

Terraform (HCL)

DevOps / CI/CD

GitHub Actions, Docker

Security Audit

Trivy Vulnerability Scanner

Backend

Python 3.12, Flask

Frontend

Tailwind CSS (Responsive Dashboard)

🚦 The DevSecOps Lifecycle

Code Commit: Developer pushes code to the repository.

Build Phase: Docker builds a hardened image using a multi-stage process.

Audit Phase: Trivy scans the image against the latest CVE databases.

Security Gate: If vulnerabilities exceed the threshold, the build is killed, and an alert is generated.

Deployment: (Success State) Verified secure images are pushed and deployed to Azure Web Apps.

📊 Project Visuals

The Security Dashboard

Shows real-time system metadata and security posture directly from the container.

The Automated Security Gate

Proof of the pipeline blocking insecure dependencies in the GitHub Actions log.

💡 Engineering Challenges Overcome

Regional Policy Restrictions: Navigated Azure Student Subscription regional quota limitations (RequestDisallowedByAzure) by architecting a provider-agnostic container solution that can be deployed to any compliant region.

Port Optimization: Resolved macOS AirPlay port conflicts by reconfiguring the application to utilize port 5001, ensuring seamless local development on Apple Silicon.

👨‍💻 Contact & Portfolio

Pradyum Samal MS Cybersecurity Engineering Student @ Illinois Institute of Technology

LinkedIn: https://www.linkedin.com/in/pradyum-samal-954599283/

GitHub: github.com/Pradyum-1712
