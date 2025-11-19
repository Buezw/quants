# Auto-generated meta weights (XGB-distilled linear) for Stock_D
import numpy as np

FEATURES = ['ret_1d', 'ret_5d', 'mom_3', 'mom_5', 'mom_10', 'roc_5', 'ma_3', 'ma_5', 'ma_10', 'ema_3', 'ema_5', 'ema_10', 'ema_20', 'vol_5', 'vol_10', 'slope_5', 'slope_10', 'rsi_14', 'macd', 'macd_signal', 'macd_hist', 'bb_pos']
WEIGHTS = np.array([223.64100833945344, -133.02032575448055, 9.824505440332594, 1.6674373452311764, 0.38738078196618075, -133.02032575451707, -53.91933797603181, 113.12159836895925, -22.753238626240663, -163.52526074539483, 176.3596661522332, -23.953255122421577, -25.382472498083057, 0.549458205977361, 0.1053571300827147, 114.16995389757568, -37.2532160456853, 0.13071837926598592, -33.69674945757087, 4.359605183718057, -38.05635464137319, -1.9978062112989148])
BIAS = 0.5871336228521125

def predict(features_dict):
    x = np.array([features_dict[f] for f in FEATURES])
    return float(np.dot(x, WEIGHTS) + BIAS)
