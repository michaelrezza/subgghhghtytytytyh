import json
from datetime import datetime

with open("subscriptions.json", "r") as f:
    data = json.load(f)

now = datetime.utcnow()
active = [s for s in data if datetime.fromisoformat(s["expires"]) > now]

with open("subscriptions.json", "w") as f:
    json.dump(active, f, indent=2)

# Regenerate index.html
with open("index.html", "w") as f:
    f.write("<!DOCTYPE html><html><head><title>Subscriptions</title></head><body><ul>")
    for sub in active:
        f.write(f'<li><a href="{sub["url"]}">{sub["name"]}</a> - {sub["expires"]}</li>')
    f.write("</ul></body></html>")
