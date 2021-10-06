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
    #    message.append(str(wallet['name']) + ' ' + str(wallet['native_balance']))
    #    print(str(wallet['native_balance']))
        value = str(wallet['native_balance']).replace('USD', '')
        total += float(value)
    
    message.append('Total Balance: ' + 'USD ' + str(total))
    print('\n'.join(message))

except AuthenticationError:
    print("Could not authenticate with your Coinbase API.")