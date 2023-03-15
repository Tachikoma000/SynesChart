import requests

def get_bitcoin_market_chart(days):
    url = f'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days={days}&interval=daily'
    headers = {
        'accept': 'application/json'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Request failed with status code {response.status_code}')

# # Call the function with 438 days of market data
# data = get_bitcoin_market_chart(438)

# # Print the response data
# print(data)

