# Sentinel Intelligence System 🛡️

Sentinel is an automated web-intelligence pipeline that monitors specific web sources (like Wikipedia), processes changes using a local AI (LLM), and pushes summarized alerts directly to your mobile device.

## 🚀 Key Features
- **Continuous Monitoring:** Runs as a persistent Windows Service to track updates 24/7.
- **Local AI Summarization:** Uses a local LLM API to distill long-form web content into concise summaries.
- **Mobile Integration:** Leverages the Pushbullet REST API for instant cross-platform notifications.
- **Config-Driven Design:** Users can manage tracking targets via `urls.txt` without touching the source code.

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **APIs:** Pushbullet API, Local LLM API
- **Libraries:** `requests`, `plyer`, `os`, `time`
- **Version Control:** Git/GitHub

## 📋 Installation & Setup

### 1. Prerequisites
- Python 3.10+
- A [Pushbullet](https://www.pushbullet.com/) account and Access Token.

### 2. Installation
Clone the repository and install dependencies:
```bash
git clone [https://github.com/Gedam12/Sentinel-Intelligence-System.git](https://github.com/Gedam12/Sentinel-Intelligence-System.git)
cd Sentinel-Intelligence-System
pip install -r requirements.txt
