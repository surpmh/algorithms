# 조합 0의 개수
import sys
import math
input = sys.stdin.readline

def countNum(n, k):
    count = 0
    while n != 0:
        n = n // k
        count += n
    return count

def main():
    n, m = map(int, input().split())
    
    count2 = countNum(n, 2) - countNum(m, 2) - countNum(n - m, 2)
    count5 = countNum(n, 5) - countNum(m, 5) - countNum(n - m, 5)

    print(min(count2, count5))

if __name__ == "__main__":
    main()