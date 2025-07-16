# strategy.py

from binance.enums import *

def momentum_strategy(client, symbol):
    """
    Simple momentum strategy:
    If last candle close > previous -> Buy
    If last candle close < previous -> Sell
    """

    # Fetches recent candle data
    try:
        candles = client.futures_klines(symbol=symbol, interval='1m', limit=3)
        prev_close = float(candles[-2][4])
        last_close = float(candles[-1][4])
        
        # Compares last two candle close prices
        # if price is rising - return BUY
        if last_close > prev_close:
            return SIDE_BUY
        # if falling - return SELL
        elif last_close < prev_close:
            return SIDE_SELL
        else:
            return None
    except Exception as e:
        print(f"Strategy error: {e}")
        return None
