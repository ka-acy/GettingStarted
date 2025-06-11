import requests

def get_crypto_data(vs_currency="usd", limit=10):
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": vs_currency,
        "order": "market_cap_desc",
        "per_page": limit,
        "page": 1,
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()
