#install the following
#pip install coinbase
from coinbase.wallet.client import Client
from Keys import coinbase_API_key, coinbase_API_secret
from coinbase.wallet.error import AuthenticationError

client = Client(coinbase_API_key, coinbase_API_secret)

total = 0
message =[]

try:
    accounts = client.get_accounts()
    #print(str(accounts)) #<-- print the entire account data
    
    for wallet in accounts.data:
        if wallet.currency == "ETH":
            value1 = str(wallet['native_balance']).replace('USD', '')
            print("%s: %s " % (wallet.name, value1))
            amt1 = float(value1)
        elif wallet.currency == "DOGE":
            value2 = str(wallet['native_balance']).replace('USD', '')
            amt2 = float(value2)
            print("%s: %s " % (wallet.name, value2))

    total = float(amt1+amt2)
    message.append('Total Balance: ' + '$' + str(total))
    print('\n'.join(message))

except AuthenticationError:
    print("Could not authenticate with your Coinbase API.")
