def factorial(x):
    if x > 1:
        # Recursive Case
        return x * factorial(x - 1)
    else:  # Base Case
        return 1


def main():
    print(factorial(5))
    return


if __name__ == "__main__":
    main()
