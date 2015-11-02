# Trace the execution of the last version of print_mult_table and figure out how it works.

def print_multiples(n, high):
    for i in range(1, high+1):
        print(n * i, end="\t")
    print()

def print_mult_table(high):
    for i in range(1, high+1):
        print_multiples(i, i)


print_mult_table(10)
#print_multiples(2,10)