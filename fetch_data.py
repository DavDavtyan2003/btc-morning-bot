import requests
import pandas as pd

def get_btc_data(interval=60, limit=100):
    # Kraken interval is in minutes: 1, 5, 15, 30, 60, 240, 1440, etc.
    url = "https://api.kraken.com/0/public/OHLC"
    params = {
        "pair": "XBTUSD",
        "interval": interval
    }
    response = requests.get(url, params=params)
    data = response.json()

    if data.get("error"):
        raise Exception(f"Kraken API error: {data['error']}")

    result_key = [k for k in data["result"].keys() if k != "last"][0]
    rows = data["result"][result_key]

    df = pd.DataFrame(rows, columns=[
        "time", "open", "high", "low", "close", "vwap", "volume", "count"
    ])

    df["time"] = pd.to_datetime(df["time"], unit="s")
    for col in ["open", "high", "low", "close", "volume"]:
        df[col] = df[col].astype(float)

    df.set_index("time", inplace=True)
    df = df[["open", "high", "low", "close", "volume"]]

    return df.tail(limit)

if __name__ == "__main__":
    df = get_btc_data()
    print(df.tail())