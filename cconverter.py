import json as j
import requests as r

first_code = input()
json_rate = r.get(f"https://www.floatrates.com/daily/{first_code}.json")
rates = j.loads(json_rate.text)
cache = {}
try:
    cache["usd"] = float(rates['usd']['rate'])
except KeyError:
    pass
try:
    cache["eur"] = float(rates['eur']['rate'])
except KeyError:
    pass

run = True

while run:
    code = input()
    if code == "":
        run = False
        break
    money = int(input())
    print("Checking the cache...")
    if code in cache.keys():
        print("Oh! It is in the cache!")
        received = round((money * cache[code]), 2)
    else:
        print("Sorry, but it is not in the cache!")
        cache[code] = float(rates[code.lower()]['rate'])
        received = round((money * cache[code]), 2)
    print(f"You received {received} {code}.")
