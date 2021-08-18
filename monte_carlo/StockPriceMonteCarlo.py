import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

TRADE_DAYS_IN_YEAR = 252
NUM_OF_SIMULATIONS = 1000

def stock_monte_carlo(S0, mu, sigma, N=TRADE_DAYS_IN_YEAR):
    result = []
    t = 1
    # number of simulations - possible S(t) realizations (of the process)
    for _ in range(NUM_OF_SIMULATIONS):
        prices = [S0]
        for _ in range(N):
            # we simulate change day by day thats why t = 1
            stock_price = prices[-1] * np.exp((mu - 0.5 * sigma ** 2)*t + sigma * np.random.normal())

            prices.append(stock_price)
        result.append(prices)
    simulation_data = pd.DataFrame(result)
    simulation_data = simulation_data.T

    simulation_data['mean'] = simulation_data.mean(axis=1)

    plt.plot(simulation_data['mean'])
    print("Prediction for future price: $%.2f" % simulation_data['mean'].tail(1))
    plt.show()

if __name__ == '__main__':
    stock_monte_carlo(50, 0.0002, 0.01)
    