# save_agents.py
import pickle

def save_agents(agents, filename="agents_data.pkl"):
    """ Save the state of all agents to a file """
    with open(filename, 'wb') as file:
        pickle.dump(agents, file)
        print(f"Data saved to {filename}")

def load_agents(filename="agents_data.pkl"):
    """ Load the state of agents from a file """
    try:
        with open(filename, 'rb') as file:
            agents = pickle.load(file)
            print(f"Data loaded from {filename}")
            return agents
    except FileNotFoundError:
        print(f"No previous data found. Starting fresh!")
        return []
