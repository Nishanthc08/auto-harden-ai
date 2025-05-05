# 🛡️ AutoHardenAI – Linux Security Auditor with AI Suggestions

**AutoHardenAI** is a powerful Linux auditing tool that automatically scans your system for misconfigurations, analyzes them using basic AI logic, and presents the results via both a CLI and a web dashboard. Designed for sysadmins, DevSecOps, and cybersecurity learners.

---

## 🚀 Features

- ✅ Automated system misconfiguration scan
- 💡 AI-generated remediation suggestions
- 📊 Terminal dashboard using `rich`
- 🌐 Web-based dashboard using Flask
- 🧠 Easily extendable for more checks and AI logic

---

## 🧰 Tech Stack

- Python 3.x
- Flask (for Web UI)
- Rich (for CLI UI)
- JSON (for data interchange)

---

## 📁 Directory Structure

autohardenai/ │ ├── audit/ │ ├── system_scan.py # Core system scanner │ └── ai_suggester.py # AI suggestion engine │ ├── dashboard/ │ ├── terminal_view.py # CLI dashboard using rich │ ├── web_dashboard.py # Web dashboard using Flask │ └── templates/ │ └── dashboard.html # HTML page for Flask UI │ ├── reports/ │ ├── latest_report.json # Output from scanner │ └── suggestions.json # AI-based suggestions


---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/yourname/autohardenai.git
cd autohardenai
```
### 2. Create a Virtual Environment (Optional but recommended)

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependecies

```bash
pip install flask rich
```

### 4. Run the Audit System

Step 1 - Run the System Scanner

```bash
python3 audit/system_scan.py
```

Step 2 - Generate AI Suggestions

```bash
python3 audit/ai_suggester.py
```

### 5. View the Results

Terminal Dashboard -

```bash
python3 dashboard/terminal_view.py
```

Web Dashboard -

```bash
python3 dashboard/web_dashboard.py
```

