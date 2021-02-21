

import requests
import json


cache = { }

def request_rate(currency):
        url =  f"http://www.floatrates.com/daily/{currency}.json"
        response = requests.get(url)
        return json.loads(response.text)

def get_rate(currency_from, currency_to):
        """
        search currency_to in cache if not present update cache
        return rate
        """
        print("Checking the cache…")

        if currency_to in cache.keys():
                print("Oh! It is in the cache!")
                return cache[currency_to][currency_from]["inverseRate"]
        else:
                print("Sorry, but it is not in the cache!")
                cache[currency_to]=request_rate(currency_to)
                return  cache[currency_to][currency_from]["inverseRate"]




cache["usd"] = request_rate("usd")
cache["eur"] = request_rate("eur")

currency_from = input().lower()

if __name__ == "__main__":
        while True:
                currency = input().lower()
                if currency == "":
                        break
                amount = int(input())
                rate = get_rate(currency_from,currency)
                print(f"You received {rate * amount} {currency.upper()}.")

