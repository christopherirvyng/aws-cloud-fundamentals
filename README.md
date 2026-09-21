# AWS Cloud Fundamentals & EC2 Deployment

## 📌 Project Overview
Dokumentasi latihan praktis fondasi Linux, Networking, dan deployment Nginx Web Server serta aplikasi Python (Flask) pada AWS EC2 Instance.

---

## 🏗️ Architecture / Flow
`User (Browser)` ➔ `Internet (Port 80 / 5000)` ➔ `AWS Security Group` ➔ `EC2 Instance (Ubuntu)` ➔ `Nginx / Python App`

---

## 🚀 Steps & Execution

### 1. Linux & SSH Setup
- Memindahkan SSH Key (`labsuser.pem`) dan mengatur permission keamanan:
  ```bash
  chmod 400 labsuser.pem
