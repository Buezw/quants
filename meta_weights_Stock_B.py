# Auto-generated meta weights (XGB-distilled linear) for Stock_B
import numpy as np

FEATURES = ['ret_1d', 'ret_5d', 'mom_3', 'mom_5', 'mom_10', 'roc_5', 'ma_3', 'ma_5', 'ma_10', 'ema_3', 'ema_5', 'ema_10', 'ema_20', 'vol_5', 'vol_10', 'slope_5', 'slope_10', 'rsi_14', 'macd', 'macd_signal', 'macd_hist', 'bb_pos']
WEIGHTS = np.array([68.72412264533216, -17.001921897262328, -0.4103135305096369, 1.0213827147219474, 0.35653313519514185, -17.001921897258697, 3.099660729072539, -38.56335032364608, -39.59421100010447, -70.0988735739905, 206.99972709658954, 19.76476488005648, -81.75716674489055, 0.6491156575774547, -1.1608630113733862, -28.441568729185178, -68.15904589358475, 0.08473020357652784, -75.95521310688122, 1.5771110178864418, -77.53232412476387, -1.5664030157022755])
BIAS = 7.963435487833824

def predict(features_dict):
    x = np.array([features_dict[f] for f in FEATURES])
    return float(np.dot(x, WEIGHTS) + BIAS)
