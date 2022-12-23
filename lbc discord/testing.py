import requests
url = 'https://data.messari.io/api/v1/assets?fields=id,slug,symbol,metrics/market_data/price_usd'
resp = requests.get(url)

money = int(input("PLease enter the amount"))
data = resp.json()

data = data['data']
data = data[0]

slug = data['slug']
symbol = data['symbol']
metrics = data['metrics']
market_data = metrics['market_data']
price_usd = market_data['price_usd']
print(price_usd)




url2 = 'https://freecurrencyapi.net/api/v2/latest?apikey=b9c78bf0-55ca-11ec-bd28-fdadc2af85cf'

resp2 = requests.get(url2)
data = resp2.json()
data = data['data']

gbp = data['GBP']
print(gbp)


total = (money/gbp)/ price_usd


print(total)