from binance.client import Client
from binance.enums import *
import json
import time
import requests

api_key_rsi = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbHVlIjoiNjQ3MjBmNzE0OThkNzVkYTM2ZThmMzZmIiwiaWF0IjoxNjg1MTk2Njc1LCJleHAiOjMzMTg5NjYwNjc1fQ.D6PMHOIaCAti2hEZiFe3opj5lI1dWCl48JG3_6X_PbM'

interval = str(input('1h, 1d, or 1m for RSI interval : ')) 
   
key = f"https://api.taapi.io/rsi?secret={api_key_rsi}&exchange=binance&symbol=BTC/USDT&interval={interval}" 

price = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

rbuying = 31
rselling = 69

#api pour binance : 

apikeybn = 'HEkPluA6BuqBprJaz2AU5wwpAPWiTnBmc3nPQjbP04qWoKUAQ8wtT84pLC8VwuF8'
apisecuritybn = 'QF1TiWI3rAVcrbwhgR1kkG7BQ7MQsTPCc1NHFBxhyI2HVczgNZIXVo3Q1aK0LZYI'

client = Client(apikeybn, apisecuritybn)
my_account = client.get_account()
print("Connected to the account")


status = client.get_account_status()
#print(f'status is {status}')

#prendre le solde de usdt valable 

def usdtbalance():
    my_account = client.get_account()
    ballanceav = my_account['balances']
    for i in ballanceav:
        if str(i['asset']) == 'USDT':
            usdt = i['free']
    return usdt

def btcbalance():
    my_account = client.get_account()
    ballanceav = my_account['balances']
    for i in ballanceav:
        if str(i['asset']) == 'BTC':
            BTC = i['free']
    return BTC

print("the avaialble usdt is ", usdtbalance())
print("the bitcoin balance is", btcbalance())

tobuy = float(usdtbalance()) 
print(f"The sum of BTC to buy is: {tobuy} USDT ")

def buying():
    order = client.create_order(symbol='BTCUSDT',  side=SIDE_BUY, type=ORDER_TYPE_MARKET, quoteOrderQty= tobuy)
    print(f"Buying completed the sum bought is {tobuy} USDT, the avalaible BTC now is {btcbalance()} BTC")

def selling():
    tosell = float(btcbalance())
    tosellfixed = round(tosell, 5)
    order = client.create_order(symbol='BTCUSDT',  side=SIDE_SELL, type=ORDER_TYPE_MARKET, quantity= tosellfixed)
    print(f"Selling completed the sum sold is {tosell} BTC, the avalaible USDT now is {usdtbalance()} USDT")

#function to see how much btc is worth in usdt after buying it 
def btcvalue_bought():
    btctousdt = float(btcbalance()) 
    btcprice = float(data1['price'])
    value = btctousdt * btcprice
    commission_fee = value * 0.001 * 2
    value -= commission_fee
    return value 

while True:
    data = requests.get(key)  
    data = data.json()
    data1 = requests.get(price)
    data1= data1.json()
    print(f"BTCUSDT rsi is {data['value']} and the price is {data1['price']}")
    print("\n")
    #rsi actuel
    rsia = data['value']

    if data['value'] <= rbuying:
        print("Buying...")
        buying()
        brsi = float(data['value'])
        bbtcvalue = float(data1['price'])
        position = 1 
        break

    #elif data['value'] >= rselling :
       # print("Sell...")
        #selling()
       # break

    elif 30 < data['value'] < 70 :
        print("HOLDING")

    time.sleep(15)

if position == 1 : #position 1 means we bought btc line 81 
    while True :
        time.sleep(15)
        data = requests.get(key)  
        data = data.json()
        data1 = requests.get(price)
        data1= data1.json()

        # Valeur de btc a l'instant ou on a acheter avec + 0.4% 
        desiredprice = (bbtcvalue * 0.4 / 100) + bbtcvalue
        print("desired price to sell is : ", desiredprice)

        # prix de btc qu'on a acheter avec + 0.4% 
        #to_out = float(btcvalue_bought()) * 0.4 / 100 

        profit_loss = ((btcvalue_bought() - tobuy) / tobuy) * 100 

        print(f"The value of our BTC that we bought after commission is {btcvalue_bought()} USDT, we bought it at a price of {tobuy} USDT with a profit of {profit_loss}")

        print(f"We bought it when RSI = {brsi} and price of BTC was {bbtcvalue} the current RSI is {data['value']} and curent BTC price is {data1['price']}")
        print("\n \n")

        rsia = data['value']

        if rsia == brsi + 10 or float(data1['price']) > desiredprice:
            print("selling...")
            selling()
            print(f"We sold in a profit with 0.4% price of entry is {btcvalue_bought()} USDT, price of exit is {desiredprice} USDT")
            print(f"Total balance is {usdtbalance()}")
            break
        elif rsia == brsi - 10 or float(data1['price']) < bbtcvalue - (bbtcvalue * 5) / 100 :
            print("selling...")
            selling()
            print(f"We sold to stop loss with price of entry is {btcvalue_bought()} USDT, price of exit is {desiredprice} USDT")
            