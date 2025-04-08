import requests

urls = ["http://localhost:9090", "http://127.0.0.1:3000"]

for url in urls:
    try:
        r = requests.get(url, timeout=3)
        print(f"{url} → {r.status_code}")
    except requests.exceptions.RequestException:
        print(f"{url} → ❌ НЕДОСТУПЕН")
