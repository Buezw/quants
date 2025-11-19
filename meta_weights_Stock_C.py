# Auto-generated meta weights (XGB-distilled linear) for Stock_C
import numpy as np

FEATURES = ['ret_1d', 'ret_5d', 'mom_3', 'mom_5', 'mom_10', 'roc_5', 'ma_3', 'ma_5', 'ma_10', 'ema_3', 'ema_5', 'ema_10', 'ema_20', 'vol_5', 'vol_10', 'slope_5', 'slope_10', 'rsi_14', 'macd', 'macd_signal', 'macd_hist', 'bb_pos']
WEIGHTS = np.array([-398.8769801271106, 28.529486383541126, -23.481998316173108, 0.5361282887899975, -0.24409863640511023, 28.529486383606084, 121.06425901256218, -300.06349413471713, 2.2020418332883724, 284.65672293878504, -152.2101612821841, 14.461698423816067, 29.770673438802298, -0.43989940847667175, -0.10448386353991734, -287.4818376266746, 0.28354473429854377, 0.08107468951554936, 34.927354783757835, -3.5554829592896677, 38.48283774304158, -0.026219082849293092])
BIAS = 12.485772948211487

def predict(features_dict):
    x = np.array([features_dict[f] for f in FEATURES])
    return float(np.dot(x, WEIGHTS) + BIAS)
