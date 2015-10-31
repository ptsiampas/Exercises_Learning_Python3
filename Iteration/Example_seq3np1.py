# the Collatz conjecture
__author__ = 'petert'
def seq3np1(n):
    """ Print the 3n+1 sequence from n,
        terminating when it reaches 1.
    """
    count=0
    # initial_num=n
    while n != 1:
        #print(n, end=", ")
        if n % 2 == 0:        # n is even
            n = n // 2
        else:                 # n is odd
            n = n * 3 + 1
        count+=1
    return count


for i in range(1,1000):
    r = seq3np1(i)
    if r == 100:
         print("Inital Num: (",i,") = 100 smallest number")
         break
