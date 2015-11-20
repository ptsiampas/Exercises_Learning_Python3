def recursion_depth(number):
    print("{0}, ".format(number), end='')
    recursion_depth(number + 1)


recursion_depth(0)
