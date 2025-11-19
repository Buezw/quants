# feature_engineering_C.py
# =====================================
# 计算 C 套因子（全部可在线复现）
# =====================================

import pandas as pd
import numpy as np

def EMA(series, span):
    return series.ewm(span=span, adjust=False).mean()

def rolling_slope(s, window):
    idx = np.arange(window)
    return s.rolling(window).apply(lambda x: np.polyfit(idx, x, 1)[0], raw=False)

def RSI(series, window=14):
    delta = series.diff()
    up = delta.where(delta > 0, 0)
    down = -delta.where(delta < 0, 0)
    avg_up = up.ewm(alpha=1/window, adjust=False).mean()
    avg_down = down.ewm(alpha=1/window, adjust=False).mean()
    rs = avg_up / (avg_down + 1e-9)
    return 100 - 100/(1 + rs)

def MACD(series):
    ema12 = EMA(series, 12)
    ema26 = EMA(series, 26)
    macd = ema12 - ema26
    signal = EMA(macd, 9)
    hist = macd - signal
    return macd, signal, hist

def BB_pos(series, window=20):
    ma = series.rolling(window).mean()
    std = series.rolling(window).std()
    return (series - ma) / (2*std + 1e-9)

def compute_features(input_csv="data.csv", output_csv="training_features_C.csv"):
    df = pd.read_csv(input_csv)

    out = []

    for stock in ["Stock_A","Stock_B","Stock_C","Stock_D","Stock_E"]:
        p = df[stock].copy()
        d = pd.DataFrame({
            "Day": df["Day"],
            "Stock": stock,
            "price": p,
            "ret_1d": p.pct_change(1),
            "ret_5d": p.pct_change(5),
            "mom_3": p - p.shift(3),
            "mom_5": p - p.shift(5),
            "mom_10": p - p.shift(10),
            "roc_5": p.pct_change(5),
            "ma_3": p.rolling(3).mean(),
            "ma_5": p.rolling(5).mean(),
            "ma_10": p.rolling(10).mean(),
            "ema_3": EMA(p, 3),
            "ema_5": EMA(p, 5),
            "ema_10": EMA(p, 10),
            "ema_20": EMA(p, 20),
            "vol_5": p.rolling(5).std(),
            "vol_10": p.rolling(10).std(),
            "slope_5": rolling_slope(p, 5),
            "slope_10": rolling_slope(p, 10),
            "rsi_14": RSI(p, 14)
        })

        macd, sig, hist = MACD(p)
        d["macd"] = macd
        d["macd_signal"] = sig
        d["macd_hist"] = hist

        d["bb_pos"] = BB_pos(p)

        # y_next: 下一日收益
        d["y_next"] = d["ret_1d"].shift(-1)

        out.append(d)

    out = pd.concat(out).dropna().reset_index(drop=True)
    out.to_csv(output_csv, index=False)
    print(f"Saved {output_csv} with C-set features.")

if __name__ == "__main__":
    compute_features()
