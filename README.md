# Binance_Trading_Bot

# Binance Futures Trading Bot (Testnet)

This is a **simplified Python trading bot** for **Binance USDT-M Futures Testnet**. It allows you to place **market** and **limit** buy/sell orders via the Binance API using a simple **command-line interface (CLI)**.

---

## Features

### Connects to Binance Futures **Testnet**  
### Place **Market** and **Limit** orders  
### Supports both **Buy** and **Sell** sides  
### Accepts input via **command-line arguments**  
### Uses `.env` file for API credentials  
### Logs all requests/responses to `bot.log`  
### Fully modular and readable code

## 🆕 New Features

### 🔹 Added **Stop-Market Order** Support  
- Place conditional trades that trigger once the market reaches a specified `stop_price`.

### 🔹 Introduced **Momentum-Based Strategy Mode**  
- Basic strategy compares recent price trends to auto-select `buy` or `sell`.  
- Enable with `--strategy` flag in CLI (no need to specify side manually).

### 🔹 Extended CLI Support  
- Accepts `--stop_price` for Stop-Market orders.  
- Add `--strategy` flag for auto-trading based on live market data.
