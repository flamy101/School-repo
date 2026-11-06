import requests

api_key = "8eb8ad7f72b38fc2950fdb6b7d928d9f"



def main():
   municipality  = input("Enter a municipality: ")

   geo_url = "http://api.openweathermap.org/geo/1.0/direct?" \
   f"q={municipality}&" \
   "limit=1&" \
   f"appid={api_key}"
   
   geo_res = requests.get(geo_url)

   if geo_res.status_code == 200:
      geo_data = geo_res.json()

      lat, lon, municipality  = geo_data[0]["lat"], geo_data[0]["lon"], geo_data[0]["name"]

      weather_url = "https://api.openweathermap.org/data/2.5/weather?" \
      f"lat={lat}&" \
      f"lon={lon}&" \
      f"appid={api_key}"

      weather_res = requests.get(weather_url)
      weather_data = weather_res.json()

      description = weather_data["weather"][0]["description"]
      temp_k = weather_data["main"]["temp"]

      temp_c = temp_k - 273.15

      print(f"municipality : {municipality} || description: {description} || temperature: {temp_c:.2f} °C")

main()