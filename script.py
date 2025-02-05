import requests
from datetime import datetime

def fetch_crypto_data():
    url = "https://api.binance.com/api/v3/ticker/24hr"
    response = requests.get(url)
    data = response.json()

    usdt_pairs = [coin for coin in data if 'USDT' in coin['symbol']]
    print(f"Fetched {len(usdt_pairs)} USDT pairs at {datetime.now()}")

if __name__ == "__main__":
    fetch_crypto_data()
