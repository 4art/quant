import numpy as np
from numpy.lib.function_base import average


class OptionPricing:
    def __init__(self, S0, E, T, rf, sigma, iterations):
        self.S0, self.E, self.T, self.rf, self.sigma, self.iterations = S0, E, T, rf, sigma, iterations

    def call_option_simulation(self):
        # we have 2 colunms: first with 0s the second column will store the payoff
        # we need the first column of 0s: payoff function is max(0, S-E) for call option
        option_data = np.zeros([self.iterations, 2])

        # dimentions: 1 dimentional array with as many items as the iterations
        rand = np.random.normal(0, 1, [1, self.iterations])

        # quation for the S(t) stock price at T
        stock_price = self.S0 * \
            np.exp(self.T * (self.rf - 0.5 * self.sigma ** 2) +
                   self.sigma * np.sqrt(self.T) * rand)

        # we need S-E because we have to calculate max(S-E, 0)
        option_data[:, 1] = stock_price - self.E

        # average for the Monte-Carlo Simulation
        # max() returns the max(0, S-E) according to the formula
        average = np.sum(np.amax(option_data, axis=1)) / float(self.iterations)

        # have to use the exp(-rT) discount factor
        return np.exp(-1.0 * self.rf * self.T) * average

    def put_option_simulation(self):
        # we have 2 colunms: first with 0s the second column will store the payoff
        # we need the first column of 0s: payoff function is max(0, S-E) for call option
        option_data = np.zeros([self.iterations, 2])

        # dimentions: 1 dimentional array with as many items as the iterations
        rand = np.random.normal(0, 1, [1, self.iterations])

        # quation for the S(t) stock price at T
        stock_price = self.S0 * \
            np.exp(self.T * (self.rf - 0.5 * self.sigma ** 2) +
                   self.sigma * np.sqrt(self.T) * rand)

        # we need E-S because we have to calculate max(E-S, 0)
        option_data[:, 1] = self.E - stock_price

        # average for the Monte-Carlo Simulation
        # max() returns the max(0, S-E) according to the formula
        average = np.sum(np.amax(option_data, axis=1)) / float(self.iterations)

        # have to use the exp(-rT) discount factor
        return np.exp(-1.0 * self.rf * self.T) * average


if __name__ == '__main__':
    model = OptionPricing(100, 100, 1, 0.05, 0.2, 100000)
    call = model.call_option_simulation()
    put = model.put_option_simulation()
    print("call: $%.2f, put: $%.2f" % (call, put))
