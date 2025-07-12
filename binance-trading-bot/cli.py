# accepts CLI input
import argparse
# load api_keys and api_secret
import os
from dotenv import load_dotenv
from bot import BasicBot

# loads env varibles from .env 
load_dotenv()
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

def main():
    # checks if api keys exist, if not warn user and exits
    if not API_KEY or not API_SECRET:
        print("API_KEY or API_SECRET is missing from .env file.")
        return

    # creates parser to handle user inputs via terminal
    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")
    
    parser.add_argument('--symbol', default='BTCUSDT', help="Trading pair symbol")
    parser.add_argument('--side', choices=['buy', 'sell'], required=True, help="Order side")
    parser.add_argument('--type', choices=['MARKET', 'LIMIT'], required=True, help="Order type")
    parser.add_argument('--quantity', type=float, required=True, help="Quantity to trade")
    parser.add_argument('--price', type=float, help="Price for LIMIT orders")

    args = parser.parse_args()

    bot = BasicBot(API_KEY, API_SECRET)
    result = bot.place_order(args.symbol, args.side, args.type, args.quantity, args.price)

    if result:
        print("Order placed successfully")
    else:
        print("Order failed. Check bot.log")

if __name__ == '__main__':
    main()
