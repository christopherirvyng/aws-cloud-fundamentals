# AWS Cloud Fundamentals & EC2 Deployment

## 📌 Project Overview
Dokumentasi latihan praktis fondasi Linux, Networking, dan deployment Nginx Web Server serta aplikasi Python (Flask) pada AWS EC2 Instance.

---

## 🏗️ Architecture Overview

```text
[ User / Browser ]
        │
        ▼  (HTTP / Port 5000)
┌────────────────────────────────────────────────────────┐
│ AWS Cloud (us-east-1)                                  │
│                                                        │
│   ┌────────────────────────────────────────────────┐   │
│   │ AWS Security Group (Inbound Rule: Port 5000)   │   │
│   └──────────────────────┬─────────────────────────┘   │
│                          │                             │
│                          ▼                             │
│   ┌────────────────────────────────────────────────┐   │
│   │ EC2 Instance (Ubuntu 24.04 LTS)                │   │
│   │                                                │   │
│   │   ├── Git & GitHub Integration                 │   │
│   │   └── Python 3 + Flask Web App (Port 5000)     │   │
│   └────────────────────────────────────────────────┘   │
└────────────────────────────────────────────────────────┘
---

## 🚀 Steps & Execution

### 1. Linux & SSH Setup
- Memindahkan SSH Key (`labsuser.pem`) dan mengatur permission keamanan:
  ```bash
  chmod 400 labsuser.pem
