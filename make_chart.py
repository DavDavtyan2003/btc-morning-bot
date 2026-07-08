import mplfinance as mpf
from fetch_data import get_btc_data

def create_chart(filename="btc_chart.png"):
    df = get_btc_data(interval="1h", limit=100)

    mpf.plot(
        df,
        type="candle",
        style="charles",
        title="BTC/USDT - Last 100 Hours",
        ylabel="Price (USDT)",
        volume=True,
        savefig=dict(fname=filename, dpi=150, bbox_inches="tight")
    )

    return filename

if __name__ == "__main__":
    path = create_chart()
    print(f"Chart saved to {path}")