def factorial(n):
    if n <= 0:
        return 1

    return factorial(n-1)*n

if __name__ == "__main__":
    for i in range(1,6):
        print(factorial(i))