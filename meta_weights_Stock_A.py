# Auto-generated meta weights (XGB-distilled linear) for Stock_A
import numpy as np

FEATURES = ['ret_1d', 'ret_5d', 'mom_3', 'mom_5', 'mom_10', 'roc_5', 'ma_3', 'ma_5', 'ma_10', 'ema_3', 'ema_5', 'ema_10', 'ema_20', 'vol_5', 'vol_10', 'slope_5', 'slope_10', 'rsi_14', 'macd', 'macd_signal', 'macd_hist', 'bb_pos']
WEIGHTS = np.array([410.1803148398336, -256.8315981958379, 50.60188408936558, 3.0312251369363055, -0.15881593438746053, -256.83159819586905, -261.06337448840446, 677.7927814392388, 26.839042922433897, -538.0693573351557, 117.78864500982861, -18.940768289401, -4.788926803884869, 0.2919213041609878, 0.7426367388516267, 637.5806831408989, 54.91829084610874, 0.14997245042552038, -11.057495650828669, 2.7781375148635727, -13.835633165725863, 0.7388446883697001])
BIAS = 33.48202880538849

def predict(features_dict):
    x = np.array([features_dict[f] for f in FEATURES])
    return float(np.dot(x, WEIGHTS) + BIAS)
