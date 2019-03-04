import json
import requests

symbol = input('Input ticker symbol: ')

iex = 'https://iextrading.com/developer/docs/#chart'

url = 'https://api.iextrading.com/1.0/stock/{}/chart'.format(symbol)

print(url)

def stock_url(url):
    stock_dict = {}
    response = requests.get(url)
    stock = json.loads(response.text)
    for info in stock:
        with open('{}_chart.json'.format(symbol), 'w+') as stockprice_file:
            json.dump(info, stockprice_file)

#json.dump(info, '{}.json.'format(symbol))

stock_url(url)


# def open_stock():
#     stock_dict = {}
#     with open(iex_update, 'r') as stock_file:
#         data = json.load(stock_file)
#         print(stock_dict)
#     with open('{}_chart.json'.format(symbol), 'w+') as stockprice_file:
#         json.dump(stock_dict, stockprice_file)

# open_stock()


