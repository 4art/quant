from scipy import stats
from numpy import log, exp, sqrt

# S(stock price), E(strike price), t(time to exp), rf(risk free rate), sigma (vol or standart deviation)


def call_option_price(S, E, T, rf, sigma):
    # first calculate
    d1 = (log(S / E) + (rf + sigma * sigma / 2.0) * T) / (sigma * sqrt(T))
    d2 = d1-sigma*sqrt(T)
    print("d1: %s, d2: %s" % (d1, d2))
    # use the N(x) to calculate a price of the option
    return S * stats.norm.cdf(d1) - E * exp(-rf * T) * stats.norm.cdf(d2)

# S(stock price), E(strike price), t(time to exp), rf(risk free rate), sigma (vol or standart deviation)


def put_option_price(S, E, T, rf, sigma):
    # first calculate
    d1 = (log(S / E) + (rf + sigma * sigma / 2.0) * T) / (sigma * sqrt(T))
    d2 = d1-sigma*sqrt(T)
    print("d1: %s, d2: %s" % (d1, d2))
    # use the N(x) to calculate a price of the option
    return -S * stats.norm.cdf(-d1) + E * exp(-rf * T) * stats.norm.cdf(-d2)

if __name__ == '__main__':
    # underlying stock price at t=0
    S0 = 100
    # strike price 
    E = 100
    # exp in 1 year = 365
    T = 1
    # risk free rate 
    rf = 0.05
    # volatility of underlying stock
    sigma = 0.2
    # call price according to Black-Scholes model
    call = call_option_price(S0, E, T, rf, sigma)
    put = put_option_price(S0, E, T, rf, sigma)
    print("call price according to Black-Scholes model: %.2f" % call)
    print("put price according to Black-Scholes model: %.2f" % put)
    