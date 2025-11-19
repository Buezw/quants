"""
UTEFA QuantiFi - Contestant Template

This template provides the structure for implementing your trading strategy.
Your goal is to maximize portfolio value over 252 (range 0 to 251) trading days.

IMPORTANT:
- Implement your strategy in the update_portfolio() function
- You can store any data you need in the Context class
- Transaction fees apply to both buying and selling (0.5%)
- Do not modify the Market or Portfolio class structures
"""
import math
class Market:
    """
    Represents the stock market with current prices for all available stocks.
    
    Attributes:
        transaction_fee: Float representing the transaction fee (0.5% = 0.005)
        stocks: Dictionary mapping stock names to their current prices
    """
    transaction_fee = 0.005
    
    def __init__(self) -> None:
        # Initialize with 5 stocks
        # Prices will be set by the backtesting script from the CSV data
        self.stocks = {
            "Stock_A": 0.0,
            "Stock_B": 0.0,
            "Stock_C": 0.0,
            "Stock_D": 0.0,
            "Stock_E": 0.0
        }

    def updateMarket(self):
        """
        Updates stock prices to reflect market changes.
        This function will be implemented during grading.
        DO NOT MODIFY THIS METHOD.
        """
        pass


class Portfolio:
    """
    Represents your investment portfolio containing shares and cash.
    
    Attributes:
        shares: Dictionary mapping stock names to number of shares owned
        cash: Float representing available cash balance
    """
    
    def __init__(self) -> None:
        # Start with no shares and $100,000 cash
        self.shares = {
            "Stock_A": 0.0,
            "Stock_B": 0.0,
            "Stock_C": 0.0,
            "Stock_D": 0.0,
            "Stock_E": 0.0
        }
        self.cash = 100000.0

    def evaluate(self, curMarket: Market) -> float:
        """
        Calculate the total value of the portfolio (shares + cash).
        
        Args:
            curMarket: Current Market object with stock prices
            
        Returns:
            Float representing total portfolio value
        """
        total_value = self.cash
        
        for stock_name, num_shares in self.shares.items():
            total_value += num_shares * curMarket.stocks[stock_name]
        
        return total_value

    def sell(self, stock_name: str, shares_to_sell: float, curMarket: Market) -> None:
        """
        Sell shares of a specific stock.
        
        Args:
            stock_name: Name of the stock to sell (must match keys in self.shares)
            shares_to_sell: Number of shares to sell (must be positive)
            curMarket: Current Market object with stock prices
            
        Raises:
            ValueError: If shares_to_sell is invalid or exceeds owned shares
        """
        if shares_to_sell <= 0:
            raise ValueError("Number of shares must be positive")

        if stock_name not in self.shares:
            raise ValueError(f"Invalid stock name: {stock_name}")

        if shares_to_sell > self.shares[stock_name]:
            raise ValueError(f"Attempted to sell {shares_to_sell} shares of {stock_name}, but only {self.shares[stock_name]} available")

        # Update portfolio
        self.shares[stock_name] -= shares_to_sell
        sale_proceeds = (1 - Market.transaction_fee) * shares_to_sell * curMarket.stocks[stock_name]
        self.cash += sale_proceeds

    def buy(self, stock_name: str, shares_to_buy: float, curMarket: Market) -> None:
        """
        Buy shares of a specific stock.
        
        Args:
            stock_name: Name of the stock to buy (must match keys in self.shares)
            shares_to_buy: Number of shares to buy (must be positive)
            curMarket: Current Market object with stock prices
            
        Raises:
            ValueError: If shares_to_buy is invalid or exceeds available cash
        """
        if shares_to_buy <= 0:
            raise ValueError("Number of shares must be positive")
        
        if stock_name not in self.shares:
            raise ValueError(f"Invalid stock name: {stock_name}")
        
        cost = (1 + Market.transaction_fee) * shares_to_buy * curMarket.stocks[stock_name]
        
        if cost > self.cash + 0.01:
            raise ValueError(f"Attempted to spend ${cost:.2f}, but only ${self.cash:.2f} available")

        # Update portfolio
        self.shares[stock_name] += shares_to_buy
        self.cash -= cost

    def get_position_value(self, stock_name: str, curMarket: Market) -> float:
        """
        Helper method to get the current value of a specific position.
        
        Args:
            stock_name: Name of the stock
            curMarket: Current Market object with stock prices
            
        Returns:
            Float representing the total value of owned shares for this stock
        """
        return self.shares[stock_name] * curMarket.stocks[stock_name]

    def get_max_buyable_shares(self, stock_name: str, curMarket: Market) -> float:
        """
        Helper method to calculate the maximum number of shares that can be bought.
        
        Args:
            stock_name: Name of the stock
            curMarket: Current Market object with stock prices
            
        Returns:
            Float representing maximum shares that can be purchased with available cash
        """
        price_per_share = curMarket.stocks[stock_name] * (1 + Market.transaction_fee)
        return self.cash / price_per_share if price_per_share > 0 else 0


class Context:
    """
    Store any data you need for your trading strategy.
    
    This class is completely customizable. Use it to track:
    - Historical prices
    - Calculated indicators (moving averages, momentum, etc.)
    - Trading signals
    - Strategy state
    
    Example usage:
        self.price_history = {stock: [] for stock in ["Stock_A", "Stock_B", "Stock_C", "Stock_D", "Stock_E"]}
        self.day_counter = 0
    """
    
    def __init__(self) -> None:
        # PUT WHATEVER YOU WANT HERE
        # Example: Track price history for technical analysis
        self.price_history = {
            "Stock_A": [],
            "Stock_B": [],
            "Stock_C": [],
            "Stock_D": [],
            "Stock_E": []
        }
        self.day = 0


def update_portfolio(curMarket: Market, curPortfolio: Portfolio, context: Context):
    import math
    import numpy as np

    # ================================
    # 1) 记录价格
    # ================================
    for stock in curMarket.stocks:
        context.price_history[stock].append(curMarket.stocks[stock])

    if context.day < 25:
        context.day += 1
        return

    # ================================
    # 2) 工具函数
    # ================================
    def EMA(values, span):
        alpha = 2 / (span + 1)
        ema = values[0]
        for v in values[1:]:
            ema = alpha * v + (1 - alpha) * ema
        return ema

    def rolling_slope(arr):
        n = len(arr)
        x = list(range(n))
        xm = sum(x) / n
        ym = sum(arr) / n
        num = sum((x[i] - xm) * (arr[i] - ym) for i in range(n))
        den = sum((x[i] - xm) ** 2 for i in range(n)) + 1e-9
        return num / den

    def RSI(values):
        gains, losses = [], []
        for i in range(1, len(values)):
            diff = values[i] - values[i - 1]
            gains.append(max(diff, 0))
            losses.append(max(-diff, 0))
        avg_gain = sum(gains) / len(gains) + 1e-9
        avg_loss = sum(losses) / len(losses) + 1e-9
        rs = avg_gain / avg_loss
        return 100 - 100 / (1 + rs)

    # ================================
    # 3) Multi-model (5 stocks → 5 models)
    #    From your uploaded files
    # ================================
    FEATURES = [
        'ret_1d', 'ret_5d',
        'mom_3', 'mom_5', 'mom_10',
        'roc_5',
        'ma_3', 'ma_5', 'ma_10',
        'ema_3', 'ema_5', 'ema_10', 'ema_20',
        'vol_5', 'vol_10',
        'slope_5', 'slope_10',
        'rsi_14',
        'macd', 'macd_signal', 'macd_hist',
        'bb_pos'
    ]

    # Load your 5 model parameter sets
    MODEL_PARAMS = {
        "Stock_A": {
            "weights": np.array([410.1803148398336, -256.8315981958379, 50.60188408936558,
                                 3.0312251369363055, -0.15881593438746053, -256.83159819586905,
                                 -261.06337448840446, 677.7927814392388, 26.839042922433897,
                                 -538.0693573351557, 117.78864500982861, -18.940768289401,
                                 -4.788926803884869, 0.2919213041609878, 0.7426367388516267,
                                 637.5806831408989, 54.91829084610874, 0.14997245042552038,
                                 -11.057495650828669, 2.7781375148635727,
                                 -13.835633165725863, 0.7388446883697001]),
            "bias": 33.48202880538849
        },
        "Stock_B": {
            "weights": np.array([68.72412264533216, -17.001921897262328, -0.4103135305096369,
                                 1.0213827147219474, 0.35653313519514185, -17.001921897258697,
                                 3.099660729072539, -38.56335032364608, -39.59421100010447,
                                 -70.0988735739905, 206.99972709658954, 19.76476488005648,
                                 -81.75716674489055, 0.6491156575774547, -1.1608630113733862,
                                 -28.441568729185178, -68.15904589358475, 0.08473020357652784,
                                 -75.95521310688122, 1.5771110178864418,
                                 -77.53232412476387, -1.5664030157022755]),
            "bias": 7.963435487833824
        },
        "Stock_C": {
            "weights": np.array([-398.8769801271106, 28.529486383541126, -23.481998316173108,
                                 0.5361282887899975, -0.24409863640511023, 28.529486383606084,
                                 121.06425901256218, -300.06349413471713, 2.2020418332883724,
                                 284.65672293878504, -152.2101612821841, 14.461698423816067,
                                 29.770673438802298, -0.43989940847667175, -0.10448386353991734,
                                 -287.4818376266746, 0.28354473429854377, 0.08107468951554936,
                                 34.927354783757835, -3.5554829592896677,
                                 38.48283774304158, -0.026219082849293092]),
            "bias": 12.485772948211487
        },
        "Stock_D": {
            "weights": np.array([223.64100833945344, -133.02032575448055, 9.824505440332594,
                                 1.6674373452311764, 0.38738078196618075, -133.02032575451707,
                                 -53.91933797603181, 113.12159836895925, -22.753238626240663,
                                 -163.52526074539483, 176.3596661522332, -23.953255122421577,
                                 -25.382472498083057, 0.549458205977361, 0.1053571300827147,
                                 114.16995389757568, -37.2532160456853, 0.13071837926598592,
                                 -33.69674945757087, 4.359605183718057,
                                 -38.05635464137319, -1.9978062112989148]),
            "bias": 0.5871336228521125
        },
        "Stock_E": {
            "weights": np.array([-110.58168222293735, 5.882939420348179, -9.346603270930096,
                                 -0.09193452072612855, -0.1225318685014602, 5.88293942034509,
                                 48.553880619363085, -122.87194556104826, -4.2630531505325155,
                                 108.0150113492986, -38.547915670715774, 5.960605200473722,
                                 3.214439409146405, -0.4952466441664464, 0.0023153413612910755,
                                 -117.76349117114356, -11.315608629776793, -0.031067412198694556,
                                 5.490150712228191, -1.270767987996688,
                                 6.760918700227721, 1.0067295268895105]),
            "bias": -4.146371088948835
        }
    }

    def predict(stock, feat_dict):
        params = MODEL_PARAMS[stock]
        w = params["weights"]
        b = params["bias"]
        x = np.array([feat_dict[f] for f in FEATURES])
        return float(np.dot(x, w) + b)

    def sigmoid(z):
        try:
            return 1 / (1 + math.exp(-z))
        except OverflowError:
            return 1.0 if z > 0 else 0.0

    # ================================
    # 4) 计算因子（22 维）
    # ================================
    features = {}
    for stock in curMarket.stocks:
        prices = context.price_history[stock][-40:]

        ret1 = (prices[-1] - prices[-2]) / prices[-2]
        ret5 = (prices[-1] - prices[-6]) / prices[-6]

        mom3 = prices[-1] - prices[-4]
        mom5 = prices[-1] - prices[-6]
        mom10 = prices[-1] - prices[-11]

        roc5 = ret5

        ma3 = sum(prices[-3:]) / 3
        ma5 = sum(prices[-5:]) / 5
        ma10 = sum(prices[-10:]) / 10

        ema3 = EMA(prices[-10:], 3)
        ema5 = EMA(prices[-10:], 5)
        ema10 = EMA(prices[-10:], 10)
        ema20 = EMA(prices[-20:], 20)

        vol5 = np.std(prices[-5:])
        vol10 = np.std(prices[-10:])

        slope5 = rolling_slope(prices[-5:])
        slope10 = rolling_slope(prices[-10:])

        rsi14 = RSI(prices[-14:])

        ema12 = EMA(prices[-26:], 12)
        ema26 = EMA(prices[-26:], 26)
        macd = ema12 - ema26
        macd_signal = EMA([macd], 9)  
        macd_hist = macd - macd_signal

        ma20 = sum(prices[-20:]) / 20
        std20 = np.std(prices[-20:])
        bb_pos = (prices[-1] - ma20) / (2 * std20 + 1e-9)

        features[stock] = {
            'ret_1d': ret1, 'ret_5d': ret5,
            'mom_3': mom3, 'mom_5': mom5, 'mom_10': mom10,
            'roc_5': roc5,
            'ma_3': ma3, 'ma_5': ma5, 'ma_10': ma10,
            'ema_3': ema3, 'ema_5': ema5, 'ema_10': ema10, 'ema_20': ema20,
            'vol_5': vol5, 'vol_10': vol10,
            'slope_5': slope5, 'slope_10': slope10,
            'rsi_14': rsi14,
            'macd': macd, 'macd_signal': macd_signal, 'macd_hist': macd_hist,
            'bb_pos': bb_pos
        }

    # ================================
    # 5) ML 概率（5 模型独立预测）
    # ================================
    scores = {}
    probs = {}
    for stock in curMarket.stocks:
        score = predict(stock, features[stock])
        prob = sigmoid(score)
        scores[stock] = score
        probs[stock] = prob

    # ================================
    # 6) 初始权重（基于概率）
    # ================================
    TH = 0.53  
    SCALE = 0.30

    target_w = {
        s: (probs[s] - TH) * SCALE if probs[s] > TH else 0.0
        for s in probs
    }

    tw_sum = sum(target_w.values())
    if tw_sum > 0:
        target_w = {s: target_w[s] / tw_sum for s in target_w}

    # ================================
    # 7) 风控软过滤
    # ================================
    final_w = {}
    for stock in target_w:
        prices = context.price_history[stock]

        ema10 = EMA(prices[-20:], 10)
        ema20 = EMA(prices[-20:], 20)
        trend_factor = 1.0 if ema10 > ema20 else 0.4

        last20 = prices[-20:]
        peak = max(last20)
        dd = (last20[-1] - peak) / peak
        dd_factor = 0 if dd < -0.15 else 1.0

        past10 = prices[-10:]
        down_days = sum(past10[i] < past10[i - 1] for i in range(1, 10))
        down_factor = 0.3 if down_days >= 7 else 1.0

        vol = np.std(prices[-20:])
        vol_target = 0.03
        vol_factor = min(1.0, vol_target / (vol + 1e-9))

        w = target_w[stock]
        w *= trend_factor
        w *= dd_factor
        w *= down_factor
        w *= (0.5 + 0.5 * vol_factor)

        final_w[stock] = w

    fw_sum = sum(final_w.values())
    if fw_sum > 0:
        final_w = {s: final_w[s] / fw_sum for s in final_w}

    # ================================
    # 8) 仓位平滑 + 强 Dead Zone + 更严格日变化限制
    # ================================
    if not hasattr(context, "prev_w"):
        context.prev_w = {s: 0 for s in curMarket.stocks}

    DEAD_ZONE = 0.06               # 最小权重变化 6%
    MAX_DAILY_DELTA = 0.03         # 每日最多调 3%

    smoothed_w = {}
    for s in final_w:
        prev = context.prev_w[s]
        target = final_w[s]

        new_w = 0.7 * prev + 0.3 * target

        if abs(new_w - prev) < DEAD_ZONE:
            new_w = prev

        # 最大每日变化幅度限制
        delta = new_w - prev
        if delta > MAX_DAILY_DELTA:
            new_w = prev + MAX_DAILY_DELTA
        elif delta < -MAX_DAILY_DELTA:
            new_w = prev - MAX_DAILY_DELTA

        smoothed_w[s] = new_w

    context.prev_w = smoothed_w

    # ================================
    # 9) 调仓执行（7 天一次 & 更高阈值）
    # ================================

    # 每 7 天调仓一次
    if context.day % 7 != 0:
        context.day += 1
        return

    total_value = curPortfolio.evaluate(curMarket)
    MIN_TRADE_VALUE = total_value * 0.007  # 每次至少 0.7% 才交易

    for stock in curMarket.stocks:
        desired_value = smoothed_w[stock] * total_value
        current_value = curPortfolio.get_position_value(stock, curMarket)
        diff = desired_value - current_value

        if abs(diff) < MIN_TRADE_VALUE:
            continue

        price = curMarket.stocks[stock]
        shares = diff / price

        if shares > 0:
            max_buy = curPortfolio.get_max_buyable_shares(stock, curMarket)
            b = min(shares, max_buy)
            if b > 1e-6:
                curPortfolio.buy(stock, b, curMarket)
        else:
            s = min(-shares, curPortfolio.shares[stock])
            if s > 1e-6:
                curPortfolio.sell(stock, s, curMarket)

    context.day += 1





###SIMULATION###
if __name__ == "__main__":
    market = Market()
    portfolio = Portfolio()
    context = Context()

    # Simulate 252 trading days (one trading year)
    for day in range(252):
        update_portfolio(market, portfolio, context)
        market.updateMarket()

    # Print final portfolio value
    final_value = portfolio.evaluate(market)
    print(f"Final Portfolio Value: ${final_value:,.2f}")
