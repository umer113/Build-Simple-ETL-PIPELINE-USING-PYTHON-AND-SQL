import requests

# Adjust the cnt parameter to increase the number of data points
url = f"https://api.openweathermap.org/data/2.5/forecast?q=los%20angeles&units=imperial&cnt=40&appid=7b26c92417fd3678d52eac12dc870222"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Request failed with status code: {response.status_code}")
