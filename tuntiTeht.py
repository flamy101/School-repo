import requests

pokemon = input("Enter pokemon name: ").lower()

url = f"https://pokeapi.co/api/v2/pokemn/{pokemon}/"
res = requests.get(url)

try:
    if res.status_code == 200:
        data = res.json()

        print(f"Type:", data["types"][0]["type"]["name"])

    else:
        print("Pokemon not found.")
except requests.exceptions.ConnectionError as error:
    print(error)
