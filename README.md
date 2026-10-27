# 🛡️ Phantom-The-System

> **Advanced Tactical Security Operations & Automation Framework**  
> *Developed by Commander Phantom*

---

## 🚀 Overview
**Phantom-The-System** is a modular, Python-based cybersecurity and tactical operations framework designed to run efficiently inside mobile and desktop terminal environments (such as Termux). It integrates multiple specialized security modules under a centralized command interface, allowing seamless vulnerability assessment, port auditing, and local lab testing with automated logging and reporting.

---

## 🛠️ Core Architecture & Modules

The framework is built with a clean, modular object/script architecture:

1. **`phantom_copilot.py` (Central Command Room & Tactical Dashboard)**
   * Central operations menu styled with a custom Neon Blue/Dark aesthetic.
   * Built-in **Tactical Security Dashboard & Log Manager** to monitor scan metrics, view reports, and securely wipe/manage logs.
   
2. **`phantom_scanner.py` (Web Vulnerability & Header Scanner)**
   * Scans target URLs for critical security headers (`X-Frame-Options`, `Content-Security-Policy`, etc.).
   * Includes automated URL input validation and error-handling.
   * Tests endpoints for basic Reflected XSS vulnerabilities and auto-logs results.

3. **`phantom_ports.py` (Fast TCP Port Audit Module)**
   * Performs quick TCP socket scans across standard operational ports (e.g., `21`, `22`, `80`, `443`, `3306`, `5000`, `8080`).
   * Automatically compiles and appends audit results to the central logging system.

4. **`weaker_app.py` (Local Vulnerable Lab)**
   * A lightweight Flask-based local web application featuring intentional vulnerable endpoints (`/greet`, `/admin`, `/leak`) to safely test and demonstrate scanner capabilities.

5. **`phantom_report.txt` (Centralized Intelligence Log)**
   * Unified auto-logging backend that records timestamps, target metadata, and vulnerability findings for post-operation review.

---

## ⚙️ Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/aboodeegms-byte/Phantom-The-System.git](https://github.com/aboodeegms-byte/Phantom-The-System.git)
   cd Phantom-The-System

