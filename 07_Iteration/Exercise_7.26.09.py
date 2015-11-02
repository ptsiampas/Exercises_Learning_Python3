# Write a function print_triangular_numbers(n) that prints out the first n triangular numbers.
# A call to print_triangular_numbers(5) would produce the following output:
#
# 1       1
# 2       3
# 3       6
# 4       10
# 5       15
# (hint: use a web search to find out what a triangular number is.)
# https://en.wikipedia.org/wiki/Triangular_number

def print_triangular_numbers(n):
    for i in range(1,n+1):
        trangular = i*(i+1)/2
        print("{0}\t{1}".format(i,trangular))

print_triangular_numbers(10)