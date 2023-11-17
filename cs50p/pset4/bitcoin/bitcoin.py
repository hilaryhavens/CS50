import requests
import sys
import json

# Error checking
# If wrong number of inputs, exit
if len(sys.argv) != 2:
    print("Missing command-line argument")
    sys.exit(1)

# If float was not inputed, exit
try:
    n = float(sys.argv[1])
except ValueError:
    print("Command-line argument is not a number")
    sys.exit(1)

# Queries the API for the CoinDesk Bitcoin Price Index
try:
    value = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    bitcoin = value['bpi']['USD']['rate_float']

# Error checking for exception
except requests.RequestException:
    pass

# Multiplies bitcoin cost by user input
cost = n * float(bitcoin)

# Outputs the current cost of Bitcoins in USD to four decimal places, using , as a thousands separator
print(f"${cost:,.4f}")