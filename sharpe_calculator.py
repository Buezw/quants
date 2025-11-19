import pandas as pd
import numpy as np

def compute_sharpe(csv_path, risk_free=0.0):
    """
    读取每日组合价值 CSV 并计算 Sharpe Ratio

    参数：
        csv_path: CSV 文件路径，要求包含列：Day, Portfolio_Value
        risk_free: 日化无风险利率（默认为 0）

    返回：
        sharpe, mean_daily_return, std_daily_return
    """
    df = pd.read_csv(csv_path)

    # 计算每日收益率
    df['ret'] = df['Portfolio_Value'].pct_change()

    # 去掉第一天的 NaN
    returns = df['ret'].dropna()

    mean_ret = returns.mean()
    std_ret = returns.std()

    if std_ret == 0:
        raise ValueError("Standard deviation is zero — Sharpe undefined.")

    # 年化 Sharpe
    sharpe = (mean_ret - risk_free) / std_ret * np.sqrt(252)

    return sharpe, mean_ret, std_ret


if __name__ == "__main__":
    # 修改这里：放你的 CSV 文件路径
    csv_file = "UTEFA_QuantiFi_Contestant_Template_daily_values.csv"

    sharpe, mean_ret, std_ret = compute_sharpe(csv_file)

    print("========== Sharpe Ratio Report ==========")
    print(f"Mean Daily Return: {mean_ret:.6f}")
    print(f"Daily Volatility:  {std_ret:.6f}")
    print(f"Sharpe Ratio:      {sharpe:.4f}")
    print("=========================================")
