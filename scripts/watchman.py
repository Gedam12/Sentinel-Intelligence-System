import time
import requests
import os
from plyer import notification

# --- DYNAMIC CONFIGURATION LOADER ---
# This ensures the script finds files in the same folder as the script itself
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE = os.path.join(BASE_DIR, "config.txt")
URL_FILE = os.path.join(BASE_DIR, "urls.txt")

def load_settings():
    """Loads the Pushbullet Token and URLs from external text files"""
    # 1. Load Token
    token = "YOUR_TOKEN_HERE"
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            token = f.read().strip()
    
    # 2. Load URLs
    urls = []
    if os.path.exists(URL_FILE):
        with open(URL_FILE, "r") as f:
            urls = [line.strip() for line in f.readlines() if line.strip()]
    else:
        # Default if file is missing
        urls = ["https://en.wikipedia.org/wiki/Artificial_intelligence"]
        
    return token, urls

# Initialize settings
PB_ACCESS_TOKEN, TARGET_URLS = load_settings()
API_URL = "http://127.0.0.1:8000/scrape"
WAIT_TIME = 900  # 15 minutes

def send_notification(title, message, link_url):
    """Sends a professional mobile push with a clickable link"""
    try:
        # Mobile Push via Pushbullet
        url = "https://api.pushbullet.com/v2/pushes"
        headers = {"Access-Token": PB_ACCESS_TOKEN, "Content-Type": "application/json"}
        payload = {
            "type": "link",
            "title": title,
            "body": message,
            "url": link_url
        }
        requests.post(url, headers=headers, json=payload)
        print(f"--- Alert Sent: {title} ---")
    except Exception as e:
        print(f"Notification Error: {e}")

def run_watchman():
    print(f"--- SENTINEL ACTIVE: Monitoring {len(TARGET_URLS)} sources ---")
    
    while True:
        # Refresh URL list every loop in case user edited urls.txt
        _, current_urls = load_settings()
        
        for url in current_urls:
            try:
                print(f"Scanning: {url}")
                response = requests.post(API_URL, params={"url": url})
                
                if response.status_code == 200:
                    data = response.json()
                    send_notification(
                        title=f"Update: {data.get('title')}",
                        message=data.get('summary', 'New intel gathered.'),
                        link_url=url
                    )
                else:
                    print(f"Server error on {url}")
            except Exception as e:
                print(f"Connection lost: {e}")
        
        time.sleep(WAIT_TIME)

if __name__ == "__main__":
    run_watchman()