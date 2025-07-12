# bot.py

# binance api client
from binance.client import Client
# order types - like market, limit
from binance.enums import *
# log activity tracking
from logger import setup_logger

# logger instance - log message to logger file
logger = setup_logger()

class BasicBot:
    # constaructor
    def __init__(self, api_key, api_secret, testnet=True):
        # initialize binance client with api keys
        self.client = Client(api_key, api_secret)
        # for testnet - use the testnet base URL 
        if testnet:
            self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'
        # log message
        logger.info("Connected to Binance Futures Testnet")
    
    # Market and limit order
    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            # Prepares order parameters 
            # Convert buy/sell string to enum like SIDE_BUY
            order_params = {
                'symbol': symbol,
                'side': SIDE_BUY if side.lower() == 'buy' else SIDE_SELL,
                'type': order_type,
                'quantity': quantity
            }
            # If it’s a LIMIT order, you must provide a price and a time-in-force policy (GTC = Good Till Cancelled).
            if order_type == ORDER_TYPE_LIMIT:
                order_params['price'] = price
                order_params['timeInForce'] = TIME_IN_FORCE_GTC

            # order logs
            logger.info(f"Placing order: {order_params}")
            # calls futures_create_order api to place order 
            order = self.client.futures_create_order(**order_params)
            # logs successfull order and return response
            logger.info(f"Order successful: {order}")
            return order
        except Exception as e:
            logger.error(f"Error placing order: {e}")
            return None
