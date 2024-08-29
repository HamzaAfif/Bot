from binance.client import Client
from binance.enums import *
import config 

apikey = 'HEkPluA6BuqBprJaz2AU5wwpAPWiTnBmc3nPQjbP04qWoKUAQ8wtT84pLC8VwuF8'
apisecurity = 'QF1TiWI3rAVcrbwhgR1kkG7BQ7MQsTPCc1NHFBxhyI2HVczgNZIXVo3Q1aK0LZYI'

client = Client(apikey, apisecurity)

print("connected") 

info = client.get_symbol_info('BTCUSDT')
exg = client.get_exchange_info()

#print(info)

#for i in info:
#    print(i)

#print("**************************************")

#symbl = info['symbol']
#print(symbl)

#print("**************************************")

my_account = client.get_account()
#print(my_account)
#for m in my_account:
#    print(m)

bal = my_account['balances']
for b in bal :
    if str(b['asset']) == 'USDT':
        usdt = b['free']

print(usdt)

status = client.get_account_status()
print(status)

fees = client.get_trade_fee() 
feess = client.get_trade_fee(symbol='BTCUSDT')

print(feess)

#order = client.create_order(symbol='BTCUSDT',  side=SIDE_BUY, type=ORDER_TYPE_MARKET, quoteOrderQty=13.48)

#order = client.create_order(symbol='BTCUSDT',  side=SIDE_SELL, type=ORDER_TYPE_MARKET, quantity= 0.00083)

def btcbalance():
    my_account = client.get_account()
    ballanceav = my_account['balances']
    for i in ballanceav:
        if str(i['asset']) == 'BTC':
            BTC = i['free']
    return BTC

print("the bitcoin balance is", btcbalance())
tosell = float(btcbalance())
tosellfixed = round(tosell, 5)

print(tosellfixed)
#order = client.create_order(symbol='BTCUSDT',  side=SIDE_SELL, type=ORDER_TYPE_MARKET, quantity= tosellfixed)