import matplotlib.pyplot as plt
import matplotlib.animation as animation
from simulator import Simulator
from save_simulation import save_simulation, load_simulation

# 🧠 Load previous simulation or create a new one
simulator = load_simulation()
if simulator is None:
    simulator = Simulator(num_agents=50)

# 🎨 Set Dark Mode
plt.style.use('dark_background')

# 🖥️ Set up figure
fig, (ax_price, ax_wealth) = plt.subplots(2, 1, figsize=(10, 8))
fig.suptitle('🌐 Market Simulation Live', fontsize=20)

days = []
prices = []
richest_agents = []

# 🧹 Clean plots first
def init():
    ax_price.clear()
    ax_price.set_title('📈 Market Price Over Time')
    ax_price.set_xlabel('Day')
    ax_price.set_ylabel('Price ($)')
    ax_price.grid(True, linestyle='--', alpha=0.5)

    ax_wealth.clear()
    ax_wealth.set_title('💰 Agent Wealth Distribution')
    ax_wealth.set_xlabel('Agents')
    ax_wealth.set_ylabel('Money ($)')
    ax_wealth.grid(True, linestyle='--', alpha=0.5)

# 🎞️ Update function for each day
def update(day):
    day += 1
    print(f"\n📅 Day {day}")

    # 🏃 Simulate one day
    simulator.run_day(day)

    # 🎯 Update market price graph
    price_today = simulator.market.get_price()
    days.append(day)
    prices.append(price_today)

    ax_price.clear()
    ax_price.plot(days, prices, color='cyan', marker='o')
    ax_price.set_title('📈 Market Price Over Time')
    ax_price.set_xlabel('Day')
    ax_price.set_ylabel('Price ($)')
    ax_price.grid(True, linestyle='--', alpha=0.5)

    # 💵 Update agent wealth distribution
    agent_wealth = [agent.money for agent in simulator.agents]
    agent_ids = [agent.id for agent in simulator.agents]

    ax_wealth.clear()
    ax_wealth.bar(agent_ids, agent_wealth, color='lime')
    ax_wealth.set_title('💰 Agent Wealth Distribution')
    ax_wealth.set_xlabel('Agent ID')
    ax_wealth.set_ylabel('Money ($)')
    ax_wealth.grid(True, linestyle='--', alpha=0.5)

    # 🎉 Show richest agent
    richest = max(simulator.agents, key=lambda a: a.money)
    print(f"🏆 Richest Agent {richest.id} with ${richest.money:.2f}")

    # 💾 Save simulation after each day
    save_simulation(simulator)

# 🚀 Animate
ani = animation.FuncAnimation(fig, update, init_func=init, frames=50, repeat=False, interval=2000)

plt.tight_layout()
plt.show()
