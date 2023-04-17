import requests

# Definir la criptomoneda y la moneda de cotización
crypto = 'bitcoin'
currency = 'usd'

# Hacer una solicitud a la API de CoinGecko para obtener los datos de precios
response = requests.get(f'https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies={currency}')

# Analizar la respuesta JSON
data = response.json()
close_price = data[crypto][currency]
