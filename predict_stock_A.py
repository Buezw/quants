import math

FEATURES = ['ret_1d', 'ret_5d', 'mom_3', 'mom_5', 'mom_10', 'roc_5', 'ma_3', 'ma_5', 'ma_10', 'ema_3', 'ema_5', 'ema_10', 'ema_20', 'vol_5', 'vol_10', 'slope_5', 'slope_10', 'rsi_14', 'macd', 'macd_signal', 'macd_hist', 'bb_pos']

def predict_stock_A(features_dict):
    features = {f: float(features_dict[f]) for f in FEATURES}

    score = 0.0

    # Tree 0
    def tree_fn(features):
