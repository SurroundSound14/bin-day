import requests
import os

IDEAL_API_KEY = os.getenv("IDEAL_POSTCODES_API_KEY")

def lookup_postcode(postcode: str):
    url = f"https://api.ideal-postcodes.co.uk/v1/postcodes/{postcode}"
    params = {"api_key": IDEAL_API_KEY}

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    result = response.json()["result"][0]

    return {
        "uprn": result["uprn"],
        "council": result["local_authority"],
        "address": result["line_1"]
    }
