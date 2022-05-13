# 링
import sys
input = sys.stdin.readline

def gcd(a, b):
    if a % b == 0:
        return b

    return gcd(b, a % b)

def main():
    n = int(input())
    r = list(map(int, input().split()))
    
    for i in range(1, n):
        g = gcd(r[0], r[i])

        print("{0}/{1}".format(r[0]//g, r[i]//g))

if __name__ == "__main__":
    main()