from scipy import stats
from numpy import log, exp, sqrt

# S(stock price), E(strike price), t(time to exp), rf(risk free rate), sigma (vol or standart deviation)


def call_option_price(S: float, E: float, T: float, rf: float, sigma: float) -> float:
    # first calculate
    d1: float = (log(S / E) + (rf + sigma * sigma / 2.0) * T) / \
        (sigma * sqrt(T))
    d2: float = d1-sigma*sqrt(T)
    print("call option d1: %s, d2: %s" % (d1, d2))
    # use the N(x) to calculate a price of the option
    sd1 = stats.norm.cdf(d1)
    sd2 = stats.norm.cdf(d2)
    e = exp(-rf * T)
    return S * stats.norm.cdf(d1) - E * exp(-rf * T) * stats.norm.cdf(d2)

# S(stock price), E(strike price), t(time to exp), rf(risk free rate), sigma (vol or standart deviation)


def put_option_price(S: float, E: float, T: float, rf: float, sigma: float) -> float:
    # first calculate
    d1: float = (log(S / E) + (rf + sigma * sigma / 2.0) * T) / \
        (sigma * sqrt(T))
    d2: float = d1-sigma*sqrt(T)
    print("put option d1: %s, d2: %s" % (d1, d2))
    # use the N(x) to calculate a price of the option
    return -S * stats.norm.cdf(-d1) + E * exp(-rf * T) * stats.norm.cdf(-d2)

def call_option_div_price(S: float, K: float, T: float, r:float, q:float, sigma: float) -> float:
    
    #S: spot price
    #K: strike price
    #T: time to maturity
    #r: interest rate
    #q: rate of continuous dividend paying asset 
    #sigma: volatility of underlying asset
    
    d1: float = (log(S / K) + (r - q + 0.5 * sigma ** 2) * T) / (sigma * sqrt(T))
    d2: float = (log(S / K) + (r - q - 0.5 * sigma ** 2) * T) / (sigma * sqrt(T))
    
    return (S * exp(-q * T) * stats.norm.cdf(d1, 0.0, 1.0) - K * exp(-r * T) * stats.norm.cdf(d2, 0.0, 1.0))
    
def put_option_div_price(S: float, K: float, T: float, r: float, q: float, sigma: float):
    
    #S: spot price
    #K: strike price
    #T: time to maturity
    #r: interest rate
    #q: rate of continuous dividend paying asset 
    #sigma: volatility of underlying asset
    
    d1 = (log(S / K) + (r - q + 0.5 * sigma ** 2) * T) / (sigma * sqrt(T))
    d2 = (log(S / K) + (r - q - 0.5 * sigma ** 2) * T) / (sigma * sqrt(T))
    
    return (K * exp(-r * T) * stats.norm.cdf(-d2, 0.0, 1.0) - S * exp(-q * T) * stats.norm.cdf(-d1, 0.0, 1.0))
    


if __name__ == '__main__':
    # underlying stock price at t=0
    S0 = 100
    # strike price
    E = 100
    # exp in 1 year = 365
    T = 1
    # risk free rate
    rf = 0.05
    #q: rate of continuous dividend paying asset 
    q = 0.5
    # volatility of underlying stock
    sigma = 0.2
    # call price according to Black-Scholes model
    call: float = call_option_price(S0, E, T, rf, sigma)
    put: float = put_option_price(S0, E, T, rf, sigma)
    print("call price according to Black-Scholes model: %.2f" % call)
    print("put price according to Black-Scholes model: %.2f" % put)
