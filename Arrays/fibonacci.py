def generate_fibonacci_iterative(n, a=0, b=1):
    for _ in range(n):
        print(a)
        a, b = b, a + b


def generate_fibonacci_recursive(n, a=0, b=1):
    if n <= 0:
        return
    print(a)
    generate_fibonacci_recursive(n - 1, b, a + b)


if __name__ == "__main__":
    print("Fibonacci Sequence (Iterative):")
    generate_fibonacci_iterative(10)

    print("\nFibonacci Sequence (Recursive):")
    generate_fibonacci_recursive(10)



