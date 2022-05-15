# 다리 놓기
import sys
input = sys.stdin.readline

def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    else:
        return 1

def main():
    t = int(input())

    for test_case in range(t):
        n, k = map(int, input().split())
        
        print(factorial(k) // (factorial(n) * factorial(k - n)))

if __name__ == "__main__":
    main()