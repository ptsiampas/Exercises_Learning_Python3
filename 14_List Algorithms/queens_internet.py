from itertools import permutations

def board(vec):
    print ("\n".join('.' * i + 'Q' + '.' * (n-i-1) for i in vec) + "\n===\n")

n = 8
cols = range(n)
for vec in permutations(cols):
    if n == len(set(vec[i]+i for i in cols)) \
         == len(set(vec[i]-i for i in cols)):
        board(vec)
        print("{0}".format(vec))
