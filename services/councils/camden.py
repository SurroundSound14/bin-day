import requests

def get_bin_collections(uprn: str):
    url = "https://www.camden.gov.uk/bin-collection-dates"
    params = {"uprn": uprn}

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()["collections"]

    return [
        {
            "bin_type": item["binType"],
            "date": item["collectionDate"]
        }
        for item in data
    ]
