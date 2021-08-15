
class CouponBonds:
    def __init__(self, principal, rate, maturity, interest_rate):
        # principal amount
        self.principal = principal
        self.rate = rate*0.01
        # date to maturity
        self.maturity = maturity
        # interest rate (discounting )
        self.interest_rate = interest_rate*0.01

    def present_value(self, x, n):
        return x / (1+self.interest_rate)**n

    def calculate_price(self):
        price = 0
        # dicount the coupon payments
        for t in range(1, self.maturity +1):
            price = price + self.present_value(self.principal * self.rate, t)
        # dicount the principal amount
        price = price + self.present_value(self.principal, self.maturity)

        return price

if __name__ == '__main__':
    principal = 1000
    rate = 10
    maturity = 3
    interest_rate = 4
    print("bond price is %.2f" % CouponBonds(principal, rate, maturity, interest_rate).calculate_price())
    