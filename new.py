import requests 
url="https://api.weatherapi.com/v1/current.json?key=e942dbeb75424295b4e94030242510&q=noida"
response = requests.get(url)
data = response.json()
print(data)
print()
print(f"TEMPERATURE : {data['current']['temp_c']}'C")
print(f"HUMIDITY : {data['current']['humidity']}")
print(f"WIND : {data['current']['wind_kph']}kph")
print(f"Feels Like : {data['current']['feelslike_c']}'C")
