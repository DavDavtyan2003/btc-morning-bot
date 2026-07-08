import requests
import pandas as pd

def get_btc_data(interval="1h", limit=100):
    url = "https://api.binance.com/api/v3/klines"
    params = {
        "symbol": "BTCUSDT",
        "interval": interval,  # e.g. 1h, 4h, 1d
        "limit": limit          # number of candles
    }
    response = requests.get(url, params=params)
    data = response.json()

    df = pd.DataFrame(data, columns=[
        "open_time", "open", "high", "low", "close", "volume",
        "close_time", "quote_asset_volume", "trades",
        "taker_buy_base", "taker_buy_quote", "ignore"
    ])

    # Convert types
    df["open_time"] = pd.to_datetime(df["open_time"], unit="ms")
    for col in ["open", "high", "low", "close", "volume"]:
        df[col] = df[col].astype(float)

    df.set_index("open_time", inplace=True)
    return df[["open", "high", "low", "close", "volume"]]

if __name__ == "__main__":
    df = get_btc_data()
    print(df.tail())