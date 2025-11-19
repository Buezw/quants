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
    """
    Implement your trading strategy here.
    """
    import math
    import numpy as np

    # =====================================================
    # 1) 记录价格历史
    # =====================================================
    for stock in curMarket.stocks:
        context.price_history[stock].append(curMarket.stocks[stock])

    if context.day < 20:
        context.day += 1
        return

    # =====================================================
    # 2) 工具函数（EMA / RSI / slope）
    # =====================================================
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

    # =====================================================
    # 3) 你的 META 权重（长度必须为 20）
    # =====================================================
    META = {
        "Stock_A": [
            0.00248, -0.00310, 0.00112, -0.00425, 0.00288,
            0.00091, -0.00177, 0.00322, -0.00239, 0.00155,
            -0.00044, 0.00083, 0.00121, -0.00210, 0.00277,
            0.00065, -0.00190, 0.00351, -0.00233, 0.00000
        ],
        "Stock_B": [
            0.00191, -0.00222, 0.00310, -0.00188, 0.00099,
            0.00142, -0.00333, 0.00211, -0.00120, 0.00117,
            -0.00142, 0.00288, -0.00255, 0.00109, -0.00071,
            0.00156, 0.00122, -0.00198, 0.00250, 0.00000
        ],
        "Stock_C": [
            0.00088, 0.00122, -0.00191, 0.00288, -0.00222,
            0.00198, 0.00210, -0.00155, 0.00314, -0.00219,
            0.00188, -0.00099, 0.00055, 0.00144, -0.00122,
            0.00281, -0.00317, 0.00244, -0.00299, 0.00000
        ],
        "Stock_D": [
            0.00210, 0.00144, -0.00281, 0.00133, -0.00104,
            0.00277, -0.00091, 0.00166, -0.00122, 0.00355,
            -0.00311, 0.00119, 0.00288, -0.00144, 0.00321,
            -0.00150, 0.00210, -0.00288, 0.00122, 0.00000
        ],
        "Stock_E": [
            0.00120, -0.00188, 0.00255, 0.00111, -0.00214,
            0.00351, -0.00177, 0.00198, 0.00211, -0.00244,
            0.00314, -0.00210, 0.00166, -0.00117, 0.00351,
            -0.00219, 0.00288, -0.00244, 0.00155, 0.00000
        ]
    }

    # =====================================================
    # 4) 生成 20 维因子
    # =====================================================
    features = {}

    for stock in curMarket.stocks:
        prices = context.price_history[stock][-30:]

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

        features[stock] = [
            ret1, ret5, mom3, mom5, mom10,
            roc5, ma3, ma5, ma10,
            ema3, ema5, ema10, ema20,
            vol5, vol10, slope5, slope10,
            rsi14, macd, macd_signal, macd_hist, bb_pos
        ]

    # =====================================================
    # 5) Meta 得分 → 概率
    # =====================================================
    def sigmoid(z):
        return 1 / (1 + math.exp(-z))

    scores = {}
    for stock in curMarket.stocks:
        w = META[stock]
        x = features[stock]
        s = sum(w[i] * x[i] for i in range(20))
        scores[stock] = s

    probs = {s: sigmoid(scores[s]) for s in scores}

    # =====================================================
    # 6) 目标权重（D 方案）
    # =====================================================
    TH = 0.52
    SCALE = 0.25

    target_w = {
        s: (probs[s] - TH) * SCALE if probs[s] > TH else 0.0
        for s in probs
    }

    tw_sum = sum(target_w.values())
    if tw_sum > 0:
        target_w = {s: target_w[s] / tw_sum for s in target_w}

    # =====================================================
    # 7) 调仓
    # =====================================================
    total_value = curPortfolio.evaluate(curMarket)

    for stock in curMarket.stocks:
        desired_value = target_w.get(stock, 0) * total_value
        current_value = curPortfolio.get_position_value(stock, curMarket)
        diff = desired_value - current_value

        if abs(diff) < 1e-6:
            continue

        price = curMarket.stocks[stock]
        shares = diff / price

        if shares > 0:  # BUY
            max_buy = curPortfolio.get_max_buyable_shares(stock, curMarket)
            buy_shares = min(shares, max_buy)
            if buy_shares > 1e-6:
                curPortfolio.buy(stock, buy_shares, curMarket)

        else:  # SELL
            sell_shares = min(-shares, curPortfolio.shares[stock])
            if sell_shares > 1e-6:
                curPortfolio.sell(stock, sell_shares, curMarket)

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
