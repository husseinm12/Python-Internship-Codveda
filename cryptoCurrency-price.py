import requests
def get_crypto_price(crypto_id, currency):
    url='https://api.coingecko.com/api/v3/simple/price'
    params = {
        'ids': crypto_id.lower(),
        'vs_currencies':currency.lower()
    }
    try:
        response = requests.get(url, params = params)
        response.raise_for_status()
        data = response.json()
        if crypto_id.lower() in data and currency.lower() in data[crypto_id.lower()]:
            price =  data[crypto_id.lower()][currency.lower()]
            print(f"\nThe current price of {crypto_id.capitalize()} in {currency.upper()} is: {price}")
        else:
            print("\nCould not find the requested crypto or currency. Check your input.")

    except requests.exceptions.HTTPError as http_err:
            print(f"\n HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
            print(f"\n Request error occurred: {req_err}")
    except ValueError:
            print("\n Error parsing the response. Please check the API or your input.")
    except Exception as err:
            print(f"\n An error occurred: {err}")
            
if __name__ == "__main__":
    print("Welcome to the Cryptocurrency Price Checker!\n")
    print("Check the price of any crypptocurrency\n")
    crypto_id = input("Enter the cryptocurrency ID (e.g., bitcoin, ethereum): ").strip()
    currency = input("Enter the currency (e.g., usd, eur): ").strip()
    get_crypto_price(crypto_id, currency)
    print("\nThank you for using the Cryptocurrency Price Checker!")
