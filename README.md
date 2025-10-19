# 🧾 QR Code Generator - Dockerized Application

## 📖 Overview
This project is a **Dockerized Python QR Code Generator** application.  
It generates QR codes based on a given URL or text input and saves the resulting images and logs inside the container.  
The project demonstrates Docker fundamentals, container security, and automated CI/CD with **GitHub Actions** and **DockerHub**.

---

## 🧱 Features
- Generates QR codes using Python (`qrcode` library)
- Automatically saves QR images and logs
- Secure Dockerfile using a non-root user
- Lightweight base image (`python:3.12-slim-bullseye`)
- Automated build and push to DockerHub using GitHub Actions

---

## 🐍 Technologies Used
- **Python 3.12**
- **Docker**
- **GitHub Actions (CI/CD)**
- **DockerHub**

---

## ⚙️ How to Run the Application

### 1. Clone the Repository
```bash
git clone https://github.com/Jvele12/qr-code-generator.git
cd qr-code-generator
```

### 2. Build the Docker Image
```bash
docker build -t qr-code-generator-app .
```

### 3. Run the Container
```bash
docker run -d --name qr-generator qr-code-generator-app
```

### 4. Check the Logs
```bash
docker logs qr-generator
```

You’ll see a message confirming a QR code was generated and saved inside `/app/qr_codes`.

To generate a custom QR code:
```bash
docker run -d --name qr-generator qr-code-generator-app --url http://www.njit.edu
```

---

## 🐳 DockerHub Repository
🔗 **Docker Image:**  
[https://hub.docker.com/repository/docker/jvele12/qr-code-generator-app](https://hub.docker.com/repository/docker/jvele12/qr-code-generator-app)

---

## 💻 GitHub Repository
🔗 **Source Code:**  
[https://github.com/Jvele12/qr-code-generator](https://github.com/Jvele12/qr-code-generator)

---

## ⚙️ GitHub Actions Workflow
The CI/CD pipeline automatically:
1. Builds the Docker image
2. Pushes it to DockerHub
3. Runs a test container for validation

Successful build example:  
✅ *“Build and Test Docker Image”* workflow completed on GitHub Actions.

---
---

## 🧠 Reflection Summary
> In this project, I learned how to package a Python application inside a Docker container, improving portability and security. I built and tested the image locally, then automated deployment to DockerHub using GitHub Actions with encrypted secrets. This process helped me understand end-to-end DevOps workflows and best practices for secure CI/CD pipelines.

---

**Author:** [Jvele12](https://github.com/Jvele12)  
**Date:** October 2025  

