def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    else:
        return 1

def main():
    num = int(input())

    print(factorial(num))

if __name__ == "__main__":
    main()