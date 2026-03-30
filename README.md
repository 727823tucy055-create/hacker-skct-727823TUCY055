# 🛡️ Honeypot Deployment Project

## 👤 Student Details

* **Name:** Vishwanth
* **Roll Number:** 727823TUCY055
* **Course:** Cyber Security Lab

---

## 📌 Project Description

This project implements a basic **Honeypot system** using Python.
A honeypot is a decoy system designed to attract attackers and monitor their activities.

In this implementation, a fake SSH service is simulated using Python sockets.
All incoming connections are logged along with timestamps to analyze attacker behavior.

---

## 🎯 Objectives

* Simulate a vulnerable SSH service
* Capture and log attacker connection attempts
* Analyze attack patterns using log data
* Demonstrate cybersecurity concepts in a controlled lab environment

---

## ⚙️ Tools & Technologies Used

* 🐍 Python (Socket Programming)
* 🐧 Kali Linux
* 🔍 Nmap (Port Scanning)
* 🔗 Netcat (Connection Testing)
* ⚡ Hydra (Brute Force Simulation)
* 💻 VirtualBox (Lab Environment)

---

## 🏗️ Project Structure

```
hacker-skct-727823TUCY055/
│
├── tool_main.py
├── setup_lab.py
├── run_tool.py
├── analyze_results.py
├── pipeline_727823TUCY055.yml
├── requirements.txt
├── README.md
├── passwords.txt
│
├── logs/
│   └── honeypot.log
│
├── screenshots/
│   ├── (all experiment screenshots)
│

```

---

## 🔐 passwords.txt

This file contains a list of passwords used for brute force simulation using Hydra.

Example content:

```
1234
admin
password
root
toor
123456
```

---

## 🚀 How to Run the Project

### 1️⃣ Setup

```bash
python3 setup_lab.py
```

### 2️⃣ Run Honeypot

```bash
python3 tool_main.py
```

### 3️⃣ Test the Honeypot

* Port Scan:

```bash
nmap <IP>
```

* Connect:

```bash
nc <IP> 2222
```

* Attack Simulation:

```bash
hydra -l admin -P passwords.txt <IP> -s 2222 ssh -t 4
```

### 4️⃣ Analyze Results

```bash
python3 analyze_results.py
```

---

## 🧪 Test Cases

| Test Case | Tool Used | Description            | Result                              |
| --------- | --------- | ---------------------- | ----------------------------------- |
| 1         | Nmap      | Port scanning          | Port 2222 detected as open          |
| 2         | Netcat    | Manual connection      | SSH banner displayed                |
| 3         | Hydra     | Brute force simulation | Multiple connection attempts logged |

---

## 📊 Output

* Honeypot logs stored in:

```
logs/honeypot.log
```

* Logs include:

  * Attacker IP address
  * Timestamp of connection
  * Multiple attack attempts

---

## ⚠️ Error Encountered

**Error:**

```
OSError: [Errno 98] Address already in use
```

**Cause:**
Port was already occupied by another process.

**Solution:**
Used the following commands:

```bash
lsof -i :2222
kill -9 <PID>
```

---

## 📈 Analysis

The honeypot successfully captured attacker interactions.
Multiple connection attempts were recorded, showing how attackers repeatedly try to access services.

Even without full SSH authentication, the system effectively monitored malicious activity.

---

## ✅ Conclusion

This project demonstrates how honeypots can be used to detect and analyze cyber attacks.
It provides a simple yet effective way to understand attacker behavior in a controlled environment.

---

## ⭐ Acknowledgment

This project was developed as part of the cybersecurity lab to understand real-world attack simulations and defensive mechanisms.
