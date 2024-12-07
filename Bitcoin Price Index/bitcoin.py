import requests
import sys


if len(sys.argv)  != 2:
    sys.exit("Missisng command-line argument")
else:
    try:
        coins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    else:
        try:
            response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        except requests.RequestException:
            sys.exit("Network Error")
        else:
            o = response.json()

            bpi = o["bpi"]
            usd = bpi["USD"]
            rate = float(usd["rate"].replace(",", ""))

            print(f"${(coins * rate):,.4f}")
            