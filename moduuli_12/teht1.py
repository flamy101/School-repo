import requests

url ="https://api.chucknorris.io/jokes/random"
res = requests.get(url)

if res.status_code == 200:
    data = res.json()
    print(f"The joke: {data["value"]}")
else:
    print(f"Error code = [{res.status_code}]")
