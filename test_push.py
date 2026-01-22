import requests 
PB_TOKEN = "o.pkhQbYgfk3KkcHoHiJjweCdLMkL87EgL" 
payload = {"type": "note", "title": "Sentinel Status: Online", "body": "Mobile alerts are working perfectly!"} 
r = requests.post("https://api.pushbullet.com/v2/pushes", headers={"Access-Token": PB_TOKEN}, json=payload) 
print("Status:", r.status_code) 
