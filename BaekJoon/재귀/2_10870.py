def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def main():
    num = int(input())

    print(fibonacci(num))

if __name__ == "__main__":
    main()