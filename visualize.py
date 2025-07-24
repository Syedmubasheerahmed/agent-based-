# visualize.py
import matplotlib.pyplot as plt

def plot_wealth_distribution(agents):
    money_list = [agent.money for agent in agents]
    
    plt.figure(figsize=(10,6))
    plt.hist(money_list, bins=15, color='gold', edgecolor='black')
    plt.title('💰 Wealth Distribution of Agents')
    plt.xlabel('Money')
    plt.ylabel('Number of Agents')
    plt.grid(True)
    plt.show()

def plot_goods_distribution(agents):
    goods_list = [agent.goods for agent in agents]
    
    plt.figure(figsize=(10,6))
    plt.hist(goods_list, bins=15, color='skyblue', edgecolor='black')
    plt.title('📦 Goods Distribution Among Agents')
    plt.xlabel('Goods')
    plt.ylabel('Number of Agents')
    plt.grid(True)
    plt.show()
