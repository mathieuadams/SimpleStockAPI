import yfinance as yf
import pandas as pd
from ta.momentum import RSIIndicator
from ta.trend import MACD


def get_stock_stats(symbol):
    data = yf.download([symbol, "SPY"], period="6mo", interval="1d", auto_adjust=True)

    stock = data['Close'][symbol].dropna()
    spy = data['Close']["SPY"].dropna()

    df = pd.DataFrame({"close": stock}).dropna()
    df["ma_10"] = df["close"].rolling(10).mean()
    df["ma_20"] = df["close"].rolling(20).mean()
    df["ma_50"] = df["close"].rolling(50).mean()

    rsi = RSIIndicator(close=df["close"]).rsi()
    macd = MACD(close=df["close"])

    correlation = stock.corr(spy)

    return {
        "symbol": symbol,
        "price": round(df["close"].iloc[-1], 2),
        "ma_10": round(df["ma_10"].iloc[-1], 2),
        "ma_20": round(df["ma_20"].iloc[-1], 2),
        "ma_50": round(df["ma_50"].iloc[-1], 2),
        "correlation_to_SPY": round(correlation, 2),
        "rsi": round(rsi.iloc[-1], 2),
        "macd": {
            "macd": round(macd.macd().iloc[-1], 2),
            "signal": round(macd.macd_signal().iloc[-1], 2),
            "histogram": round(macd.macd_diff().iloc[-1], 2)
        }
    }