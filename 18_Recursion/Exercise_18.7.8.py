# 8.Rewrite the fibonacci algorithm without using recursion. Can you find bigger terms of the sequence?
# Can you find fib(200)?
import time


def fibr(n):
    if n <= 1:
        return n
    t = fibr(n - 1) + fibr(n - 2)
    return t


def fib(x):
    first = 0
    second = 1
    for n in range(x):
        third = first + second
        second = first
        first = third
    return third


def main():
    n = 200
    # lets try some whacky timings
    t0 = time.clock()
    fr = fibr(n)
    t1 = time.clock()
    fr_time = t1 - t0

    t0 = time.clock()
    f = fib(n)
    t1 = time.clock()
    f_time = t1 - t0

    print("Recusive Fibonacci={0} in {1} Seconds.\nNon-Recursive Fibonacci={2} in {3} Seconds."
          .format(fr, fr_time, f, f_time))
    return


if __name__ == '__main__':
    main()
