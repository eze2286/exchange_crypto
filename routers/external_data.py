import requests

# Realiza una solicitud GET a la API de Coindesk
response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

# Obtén el precio del Bitcoin en USD
btc_price_usd = response.json()['bpi']['USD']['rate']
close_price = float(str(btc_price_usd).replace(",",""))


# import requests

# # Definir la criptomoneda y la moneda de cotización
# crypto = 'bitcoin'
# currency = 'usd'

# # Hacer una solicitud a la API de CoinGecko para obtener los datos de precios
# response = requests.get(f'https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies={currency}')

# # Analizar la respuesta JSON
# data = response.json()
# print(data)
# close_price = data[crypto][currency]
