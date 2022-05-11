# 어린 왕자
import sys
import math
input = sys.stdin.readline

def main():
    t = int(input())

    for test_case in range(t):
        count = 0
        x1, y1, x2, y2 = map(int, input().split())
        n = int(input())
        for _ in range(n):
            cx, cy, r = map(int, input().split())
            d1 = math.sqrt(math.pow((x1 - cx), 2) + math.pow((y1 - cy), 2))
            d2 = math.sqrt(math.pow((x2 - cx), 2) + math.pow((y2 - cy), 2))
            
            if (d1 < r and d2 > r) or (d1 > r and d2 < r):
                count += 1

        print(count)
    
if __name__ == "__main__":
    main()