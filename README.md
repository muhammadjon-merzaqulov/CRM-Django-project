# CSCI 436 – Introduction to Cloud Computing

## Assignment 3: Docker & Containerization (Django & PostgreSQL Implementation)

This repository contains the completed tasks for Assignment 3. The project demonstrates the containerization of a multi-service CRM application using **Django** for the backend and **PostgreSQL** for the database, orchestrated with **Docker Compose**.

---

## 🚀 Project Overview

The goal of this assignment is to demonstrate:

- Custom Dockerfile creation for a Django application
- Multi-container orchestration using Docker Compose
- Data persistence using Docker volumes
- Clean and professional project structure

---

## 🛠️ Tech Stack

- **Framework:** Django 5.x (Python 3.12-slim)
- **Database:** PostgreSQL 14
- **Containerization:** Docker & Docker Compose
- **Environment:** macOS (Apple Silicon optimized)

---

## 📋 Task Implementation Details

### Task 1 & 2: Docker Fundamentals & Debugging

- Verified Docker installation with:
  ```bash
  docker run hello-world
  ```
- Checked containers and images:
  ```bash
  docker ps
  docker images
  ```
- Monitored logs:
  ```bash
  docker logs ...
  ```
- Accessed container shell:
  ```bash
  docker exec -it ... bash
  ```

---

### Task 3: Custom Docker Image

- Created optimized `Dockerfile` using:
  ```
  python:3.12-slim
  ```
- Reduced image size and improved performance
- Handled static files:
  ```bash
  python manage.py collectstatic
  ```

---

### Task 4 & 5: Multi-Container System & Persistence

System architecture:

- **web service**
  - Runs Django app on port `8000`

- **db service**
  - PostgreSQL 14 database

- **Volume**
  - `postgres_data` ensures data persistence even after container removal

---

## 📂 Project Structure

```
.
├── accounts/             
├── contacts/             
├── crm_project/          
├── dashboard/            
├── deals/                
├── leads/                
├── tasks/                
├── templates/            
├── static/js/            
├── media/profile_pics/   
├── Screenshots/          
├── Dockerfile            
├── docker-compose.yml    
├── manage.py             
├── requirements.txt      
└── .dockerignore         
```

---

## ⚙️ How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/muhammadjon-merzaqulov/CRM-Django-project.git
cd CRM-Django-project
```

### 2. Build and start containers

```bash
docker-compose up --build
```

### 3. Apply migrations

```bash
docker-compose exec web python manage.py migrate
```

### 4. Open in browser

```
http://localhost:8000
```

---

## 📸 Deliverables (Screenshots)

All required outputs for Tasks 1–5 are located in the **Screenshots/** folder:

- Docker command outputs
- Build logs
- Running Django application
- Database persistence proof

---

## 🎥 Video Demonstration

A 15 minute demo video showing:

- Docker setup
- Dockerfile build
- Docker Compose execution
- Working CRM system

👉 **[Add your video link here]**

---

## 👤 Author

**Name:** Muhammadjon Merzaqulov  
**Course:** CSCI 436 – Introduction to Cloud Computing   
**Submission Date:** April 1, 2026

---
