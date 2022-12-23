import requests

url  = 'https://caiefinder.com/search/?subs=&zone=&search=A+cube'


req = requests.get(url)

print(req.content)