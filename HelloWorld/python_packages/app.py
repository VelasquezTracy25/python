import requests

url = "https://api.yelp.com/v3/businesses/search"
api_key = "8gxaaO6mptFNjNnoPCP0_lyjlK7VnkpH0QLNncycGCvk44X-MxrEKOPa0l_LUT1WcaztHeyc8rddihg4_OrPEwWIiBcl1OsrqsKTG9R0_AqczdPKv9J-LUAvsLbvZHYx"
headers = {
    "Authorization": "Bearer " + api_key
}
params = {
    "term": "Barber",
    "location": "NYC",
}
response = requests.get(url, headers=headers, params=params)
businesses = response.json()["businesses"]

names = [business["name"]
         for business in businesses if business["rating"] > 4.5]


print(names)
