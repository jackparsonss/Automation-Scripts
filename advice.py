import requests

res = requests.get("https://api.adviceslip.com/advice")

print(res.json()["slip"]["advice"])
