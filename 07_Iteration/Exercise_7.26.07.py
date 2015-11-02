# Add a print function to Newton’s sqrt function that prints out better each time it is calculated. Call your
# modified function with 25 as an argument and record the results.


def sqrt(n):
    approx = n/2.0     # Start with some or other guess at the answer
    while True:
        better = (approx + n/approx)/2.0
        if abs(approx - better) < 0.000001:
            return better
        approx = better
        print("better={0}".format(better))

# Test cases
print(sqrt(25.0))
# print(sqrt(49.0))
# print(sqrt(81.0))
