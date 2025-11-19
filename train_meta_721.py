import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import xgboost as xgb

STOCKS = ["Stock_A", "Stock_B", "Stock_C", "Stock_D", "Stock_E"]

# 你的 C 因子文件
DATA_FILE = "training_features_C.csv"

# 训练集范围（7-2-1）
TRAIN_END = 175      # 0–175 = 176 days
VAL_START = 176      # 验证集
VAL_END = 225
TEST_START = 226     # 本地测试用
TEST_END = 251

def load_data():
    df = pd.read_csv(DATA_FILE)
    # 按 Day 排序很重要
    df = df.sort_values(["Stock", "Day"]).reset_index(drop=True)
    return df

def get_feature_cols():
    return [
        "ret_1d","ret_5d","mom_3","mom_5","mom_10",
        "roc_5","ma_3","ma_5","ma_10",
        "ema_3","ema_5","ema_10","ema_20",
        "vol_5","vol_10","slope_5","slope_10",
        "rsi_14","macd","macd_signal","macd_hist","bb_pos"
    ]

def train_single_stock(df, stock):
    d = df[df["Stock"] == stock].reset_index(drop=True)
    features = get_feature_cols()

    # 切出 7:2:1
    train = d[(d["Day"] >= 0) & (d["Day"] <= TRAIN_END)]
    val   = d[(d["Day"] >= VAL_START) & (d["Day"] <= VAL_END)]
    _test = d[(d["Day"] >= TEST_START) & (d["Day"] <= TEST_END)]  # 不用于训练

    # X, y
    # X, y
    X_train = train[features].values

    # --- force binary label ---
    y_train = (train["y_next"].values > 0).astype(int)

    X_val = val[features].values
    y_val = (val["y_next"].values > 0).astype(int)


    X_val = val[features].values
    y_val = val["y_next"].values.astype(float)

    # ==============================
    # 1) 先训一个 XGBoost Teacher
    # ==============================
    xgb_model = xgb.XGBClassifier(
        n_estimators=200,
        max_depth=3,
        learning_rate=0.05,
        subsample=0.9,
        colsample_bytree=0.9,
        objective="binary:logistic",
        eval_metric="logloss",
        random_state=42,
        n_jobs=4,
    )
    xgb_model.fit(X_train, y_train)

    # 训练集上 teacher 概率
    p_train = xgb_model.predict_proba(X_train)[:, 1]
    eps = 1e-6
    p_train_clip = np.clip(p_train, eps, 1 - eps)

    # logit(p_teacher) 作为蒸馏目标
    y_logit = np.log(p_train_clip / (1 - p_train_clip))

    # ==============================
    # 2) 用线性回归拟合 logit
    #    得到 w, b（给 submission 用）
    # ==============================
    lin_model = LinearRegression()
    lin_model.fit(X_train, y_logit)

    weights = lin_model.coef_
    bias = lin_model.intercept_

    # ==============================
    # 3) 在验证集上看看蒸馏后的性能
    # ==============================
    z_val = X_val @ weights + bias
    p_val = 1.0 / (1.0 + np.exp(-z_val))

    eps2 = 1e-15
    p_val_clip = np.clip(p_val, eps2, 1 - eps2)
    # logloss
    val_logloss = -np.mean(
        y_val * np.log(p_val_clip) + (1 - y_val) * np.log(1 - p_val_clip)
    )

    print(f"{stock}: distilled XGB -> linear, val logloss = {val_logloss:.6f}")

    # ==============================
    # 4) 导出 meta_weights_Stock_X.py
    #    接口不变：FEATURES, WEIGHTS, BIAS, predict()
    # ==============================
    save_meta_weights(stock, features, weights, bias)

def save_meta_weights(stock, features, weights, bias):
    filename = f"meta_weights_{stock}.py"

    with open(filename, "w") as f:
        f.write(f"# Auto-generated meta weights (XGB-distilled linear) for {stock}\n")
        f.write("import numpy as np\n\n")
        f.write(f"FEATURES = {features}\n")
        f.write(f"WEIGHTS = np.array({weights.tolist()})\n")
        f.write(f"BIAS = {bias}\n\n")
        f.write("def predict(features_dict):\n")
        f.write("    x = np.array([features_dict[f] for f in FEATURES])\n")
        f.write("    return float(np.dot(x, WEIGHTS) + BIAS)\n")

    print(f"Saved {filename}")

def main():
    df = load_data()
    for stock in STOCKS:
        train_single_stock(df, stock)

if __name__ == "__main__":
    main()