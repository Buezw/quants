# Auto-generated meta weights (XGB-distilled linear) for Stock_E
import numpy as np

FEATURES = ['ret_1d', 'ret_5d', 'mom_3', 'mom_5', 'mom_10', 'roc_5', 'ma_3', 'ma_5', 'ma_10', 'ema_3', 'ema_5', 'ema_10', 'ema_20', 'vol_5', 'vol_10', 'slope_5', 'slope_10', 'rsi_14', 'macd', 'macd_signal', 'macd_hist', 'bb_pos']
WEIGHTS = np.array([-110.58168222293735, 5.882939420348179, -9.346603270930096, -0.09193452072612855, -0.1225318685014602, 5.88293942034509, 48.553880619363085, -122.87194556104826, -4.2630531505325155, 108.0150113492986, -38.547915670715774, 5.960605200473722, 3.214439409146405, -0.4952466441664464, 0.0023153413612910755, -117.76349117114356, -11.315608629776793, -0.031067412198694556, 5.490150712228191, -1.270767987996688, 6.760918700227721, 1.0067295268895105])
BIAS = -4.146371088948835

def predict(features_dict):
    x = np.array([features_dict[f] for f in FEATURES])
    return float(np.dot(x, WEIGHTS) + BIAS)
