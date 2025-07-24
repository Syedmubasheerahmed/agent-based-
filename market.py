# market.py
import random

class Market:
    def __init__(self, base_price=100, volatility=0.05):
        self.base_price = base_price  # Starting price
        self.volatility = volatility  # How much it can randomly move
        self.trend = 0                # Bullish, bearish or stable
        self.last_price = base_price  # ✅ Track last price for graph

    def update_trend(self):
        event = random.choices(['bull', 'bear', 'stable'], weights=[0.2, 0.2, 0.6])[0]
        if event == 'bull':
            self.trend = 1
            print("🐂 Bull Market! Prices tend to rise.")
        elif event == 'bear':
            self.trend = -1
            print("🐻 Bear Market! Prices tend to fall.")
        else:
            self.trend = 0
            print("😶 Stable Market.")

    def get_price(self):
        # 🎯 Apply trend + volatility
        trend_impact = self.trend * random.uniform(0.01, 0.03)
        random_volatility = random.uniform(-self.volatility, self.volatility)
        price_change_factor = 1 + random_volatility + trend_impact

        new_price = self.last_price * price_change_factor
        self.last_price = max(1, new_price)  # Prevent price going below 1

        return self.last_price

