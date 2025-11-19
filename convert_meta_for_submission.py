# convert_meta_for_submission.py
"""
Convert raw meta_weights_Stock_X.py (with large LinearRegression coef_)
into submission-friendly small weights for UTEFA.

It will:
 - import meta_weights_Stock_*.py
 - extract WEIGHTS and BIAS
 - compute a safe scaling factor
 - scale weights & bias
 - print final META = {...} that can be pasted into your submission
"""

import importlib
import numpy as np

STOCKS = ["Stock_A", "Stock_B", "Stock_C", "Stock_D", "Stock_E"]

def load_raw_weights(stock):
    module = importlib.import_module(f"meta_weights_{stock}")
    W = module.WEIGHTS.copy().astype(float)
    b = float(module.BIAS)
    return W, b

def scale_weights(W, b):
    """
    Scale down the raw linear model weights so that
    w·x produces a stable logit for sigmoid().
    """

    # Case 1: use max-abs scaling (common choice)
    scale = np.max(np.abs(W))

    # Prevent zeros
    if scale < 1e-9:
        scale = 1.0

    W2 = W / scale
    b2 = b / scale

    return W2, b2, scale


def main():
    print("========== META for submission ==========")
    print("META = {")

    for stock in STOCKS:
        W, b = load_raw_weights(stock)
        W2, b2, scale = scale_weights(W, b)

        # Convert numpy array to Python list
        Wlist = [float(x) for x in W2]

        print(f'    "{stock}": {Wlist},   # scaled by 1/{scale:.2f}')

    print("}")
    print("==========================================")

if __name__ == "__main__":
    main()
