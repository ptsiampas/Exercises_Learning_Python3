__author__ = 'petert'

def final_amt(p,r,n,t):
    """
    :param p:  Principle amount
    :param r: annual nominal interest rate (as decimal)
    :param n: number of times the interest is compunded per year
    :param t: number of years
    :return:
    """
    a = p * (1 + r/n)**(n*t)
    return a

toInvest = float(input("HOw much do you want to invest? "))
fnl = final_amt(toInvest, 0.08, 12, 5)
print("At the end of the peiod you'll have: ", fnl)
