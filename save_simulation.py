# save_simulation.py
# import pickle
# from simulator import Simulator

# def save_simulation(simulator, filename="simulation_data.pkl"):
#     """ Save the entire simulation state """
#     with open(filename, 'wb') as file:
#         pickle.dump(simulator, file)
#         print(f"Simulation saved to {filename}")

# def load_simulation(filename="simulation_data.pkl"):
#     """ Load the entire simulation state """
#     try:
#         with open(filename, 'rb') as file:
#             simulator = pickle.load(file)
#             print(f"Simulation loaded from {filename}")
#             return simulator
#     except FileNotFoundError:
#         print(f"No previous simulation data found. Starting fresh!")
#         return simulator()  # Default simulator if no saved data
# save_simulation.py

import pickle

def save_simulation(simulator, filename="simulation_data.pkl"):
    """ Save the entire simulation state """
    with open(filename, 'wb') as file:
        pickle.dump(simulator, file)
        print(f"Simulation saved to {filename}")

def load_simulation(filename="simulation_data.pkl"):
    """ Load the entire simulation state """
    try:
        # Import Simulator *inside* the function to avoid circular import issue
        from simulator import Simulator
        
        with open(filename, 'rb') as file:
            simulator = pickle.load(file)
            print(f"Simulation loaded from {filename}")
            return simulator
    except FileNotFoundError:
        print(f"No previous simulation data found. Starting fresh!")
        return None

