def _price():
    while True:
        try:
            price_int = float(input("What is Bitcoin price today?\n"))
            return price_int
        except ValueError:
            print("Please, enter correct course in USD ")
        
        
def _money():
    while True:
        try:
            money_int = float(input("How much $ do you have?\n"))
            return money_int
        except ValueError:
            print("Please, enter correct sum in USD")
       

def count():
    price = _price()
    money = _money()
    result = format(money/price, '.7f')
    print(f"You can buy {result} BTC")
    return result


count()
