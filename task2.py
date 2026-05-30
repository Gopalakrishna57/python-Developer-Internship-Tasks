import requests

def get_live_prices():
    # Free Crypto API URL (CoinGecko)
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=5&page=1"
    
    try:
        print("Fetching data from API... Please wait...")
        response = requests.get(url)
        
        # If response is successful (Status Code 200)
        if response.status_code == 200:
            data = response.json()
            
            print("\n" + "="*40)
            print(f"{'Coin Name':<15} | {'Current Price (USD)':<15}")
            print("="*40)
            
            for coin in data:
                print(f"{coin['name']:<15} | ${coin['current_price']:<15,}")
            print("="*40)
        else:
            print(f"Failed to fetch data. Status Code: {response.status_code}")
            
    except Exception as e:
        print("Error occurred while connecting to the network:", str(e))

if __name__ == "__main__":
    get_live_prices()