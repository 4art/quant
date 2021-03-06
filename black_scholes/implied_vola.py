import numpy as np
from scipy.stats import norm
N = norm.cdf

def bs_call(S, K, T, r, vol):
    d1 = (np.log(S/K) + (r + 0.5*vol**2)*T) / (vol*np.sqrt(T))
    d2 = d1 - vol * np.sqrt(T)
    return S * norm.cdf(d1) - np.exp(-r * T) * K * norm.cdf(d2)

def bs_vega(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    return S * norm.pdf(d1) * np.sqrt(T)

def find_vol(target_value, S, K, T, r, *args):
    MAX_ITERATIONS = 200
    PRECISION = 1.0e-5
    sigma = 0.5
    for i in range(0, MAX_ITERATIONS):
        price = bs_call(S, K, T, r, sigma)
        vega = bs_vega(S, K, T, r, sigma)
        diff = target_value - price  # our root
        if (abs(diff) < PRECISION):
            return sigma
        sigma = sigma + diff/vega # f(x) / f'(x)
    return sigma # value wasn't found, return best guess so far


if __name__ == '__main__':
    # https://stackoverflow.com/questions/61289020/fast-implied-volatility-calculation-in-python
    S = 100
    K = 100
    T = 11
    r = 0.01
    vol = 0.25

    V_market = bs_call(S, K, T, r, vol)
    implied_vol = find_vol(V_market, S, K, T, r)

    print ('Implied vol: %.2f%%' % (implied_vol * 100))
    print ('Market price = %.2f' % V_market)
    print ('Model price = %.2f' % bs_call(S, K, T, r, implied_vol))
