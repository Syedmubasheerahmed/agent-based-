# save_market.py
import pickle

def save_market(market, filename="market_data.pkl"):
    """ Save the state of the market to a file """
    with open(filename, 'wb') as file:
        pickle.dump(market, file)
        print(f"Market data saved to {filename}")

def load_market(filename="market_data.pkl"):
    """ Load the state of the market from a file """
    try:
        with open(filename, 'rb') as file:
            market = pickle.load(file)
            print(f"Market data loaded from {filename}")
            return market
    except FileNotFoundError:
        print(f"No previous market data found. Starting fresh!")
        return market()  # Default market if no saved data
