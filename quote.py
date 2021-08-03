import requests

res = requests.get("https://api.themotivate365.com/stoic-quote")

quote = res.json()["data"]

print('"' + str(quote["quote"]) + '"')

author = quote["author"]

if author is None:
    author = "unkown"

print("\n\t-" + str(author))
