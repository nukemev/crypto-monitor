import requests
from datetime import datetime

def fetch_crypto_data():
    url = "https://api.binance.com/api/v3/ticker/24hr"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise error for bad responses (4xx or 5xx)
        data = response.json()

        # Check if data is a list (expected structure)
        if isinstance(data, list):
            usdt_pairs = [coin for coin in data if 'USDT' in coin.get('symbol', '')]
            print(f"Fetched {len(usdt_pairs)} USDT pairs at {datetime.now()}")
        else:
            print("Unexpected data format:", data)

    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
    except ValueError:
        print("Error decoding JSON:", response.text)

if __name__ == "__main__":
    fetch_crypto_data()

