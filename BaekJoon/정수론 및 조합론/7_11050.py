# 이항 계수 1
import sys
input = sys.stdin.readline

def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    else:
        return 1

def main():
    n, k = map(int, input().split())

    print(factorial(n) // (factorial(k) * factorial(n - k)))

if __name__ == "__main__":
    main()