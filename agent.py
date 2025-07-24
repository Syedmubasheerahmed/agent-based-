import random

class Agent:
    def __init__(self, id):
        self.id = id
        self.money = 100  # Starting money
        self.goods = 0  # Starting goods
        self.personality = random.choice(['risk-averse', 'risk-seeking'])  # Example of personality

    def decide_action(self, price_today):
        """
        Decide whether to 'buy', 'sell', or 'save' based on the market price and personality.
        """
        if self.personality == 'risk-averse':
            # Risk-averse agents might buy when prices are low or sell when they have a lot of money
            if price_today < 100 and self.money >= price_today:
                return 'buy'
            elif self.goods > 0:
                return 'sell'
            else:
                return 'save'
        else:
            # Risk-seeking agents might take more chances in a volatile market
            if price_today < 120 and self.money >= price_today:
                return 'buy'
            elif self.goods > 0:
                return 'sell'
            else:
                return 'save'
