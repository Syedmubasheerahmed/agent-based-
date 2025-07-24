from agent import Agent
from market import Market
from save_simulation import save_simulation, load_simulation
import random

class Simulator:
    def __init__(self, num_agents=50, tax_rate=0.05):
        self.agents = [Agent(id=i) for i in range(num_agents)]
        self.market = Market()
        self.tax_rate = tax_rate

    def trigger_random_event(self):
        """
        Random events like pandemic, war, etc., that affect agents.
        """
        event = random.choice(['pandemic', 'war', 'boom', 'none'])
        if event == 'pandemic':
            print("⚡ Pandemic! All agents lose 10% of wealth.")
            for agent in self.agents:
                agent.money *= 0.9
        elif event == 'war':
            print("⚡ War! 20% of goods destroyed.")
            for agent in self.agents:
                agent.goods = max(0, agent.goods - int(agent.goods * 0.2))
        elif event == 'boom':
            print("🌟 Economic Boom! Everyone gains 15% extra wealth!")
            for agent in self.agents:
                agent.money *= 1.15
        else:
            print("🌱 No major event today.")

    def collect_taxes(self):
        """
        Government collects taxes every day.
        """
        total_tax = 0
        for agent in self.agents:
            tax = agent.money * self.tax_rate
            agent.money -= tax
            total_tax += tax
        print(f"💸 Government collected ${total_tax:.2f} in taxes.")

    def run_day(self, day_num):
        print(f"\n📅 Day {day_num}")
        self.trigger_random_event()
        self.collect_taxes()
        self.market.update_trend()  # Market trend update
        price_today = self.market.get_price()
        print(f"🛒 Market Price Today: ${price_today:.2f}")
        
        for agent in self.agents:
            action = agent.decide_action(price_today)
            if action == 'buy' and agent.money >= price_today:
                agent.goods += 1
                agent.money -= price_today
                print(f"🛒 Agent {agent.id} ({agent.personality}) bought 1 good for ${price_today:.2f}")
            elif action == 'sell' and agent.goods > 0:
                agent.goods -= 1
                agent.money += price_today
                print(f"💰 Agent {agent.id} ({agent.personality}) sold 1 good for ${price_today:.2f}")
            else:
                print(f"💾 Agent {agent.id} ({agent.personality}) chose to save.")

    def report(self):
        """
        End of Simulation Report: The richest and poorest agents, average wealth, etc.
        """
        richest = max(self.agents, key=lambda x: x.money)
        poorest = min(self.agents, key=lambda x: x.money)
        avg_wealth = sum(agent.money for agent in self.agents) / len(self.agents)
        print(f"\n🏆 Richest Agent: {richest.id} with ${richest.money:.2f}")
        print(f"💀 Poorest Agent: {poorest.id} with ${poorest.money:.2f}")
        print(f"💵 Average Wealth: ${avg_wealth:.2f}")
        print(f"💼 Total Goods in Economy: {sum(agent.goods for agent in self.agents)}")

