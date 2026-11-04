import requests

url = "8eb8ad7f72b38fc2950fdb6b7d928d9f"
res = requests.get(url)

if res.status_code == 200:
   data = res.json()
   print(data)