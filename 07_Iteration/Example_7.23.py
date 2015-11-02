def sqrt(n):
    approx = n/2.0     # Start with some or other guess at the answer
    while True:
        better = (approx + n/approx)/2.0
        if abs(approx - better) < 0.000001:
            return better
        approx = better

# Test cases
print(sqrt(2.0))
print(sqrt(3.0))
print(sqrt(4.0))
