
class ZeroCouponBonds:
    def __init__(self, principal, maturity, interest_rate):
        # principal amount
        self.principal = principal
        # date to maturity
        self.maturity = maturity
        # interest rate (discounting )
        self.interest_rate = interest_rate*0.01

    def present_value(self, x,  n):
        return x/(1+self.interest_rate)**n

    def calculate_price(self):
        return self.present_value(self.principal, self.maturity)


if __name__ == '__main__':
    principal = 1000
    maturity = 2
    interest_rate = 4
    print("principal: %s$ maturity: %s year(s), interest rate: %s percent" % (principal, maturity , interest_rate))
    print("price of a bond in dollar is %.2f" % ZeroCouponBonds(principal, maturity, interest_rate).calculate_price())
