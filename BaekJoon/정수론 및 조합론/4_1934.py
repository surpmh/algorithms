# 최소공배수
import sys
input = sys.stdin.readline

def gcd(a, b):
    if a % b == 0:
        return b

    return gcd(b, a % b)

def main():
    t = int(input())

    for test_case in range(t):
        n1, n2 = map(int, input().split())

        if n1 < n2:
            n1, n2 = n2, n1

        num = gcd(n1, n2)

        print(n1 * n2 // num)
    
if __name__ == "__main__":
    main()