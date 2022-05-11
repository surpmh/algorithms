# 앵그리 창영
import sys
import math
input = sys.stdin.readline

def main():
    n, w, h = map(int, input().split())

    for i in range(n):
        l = int(input())
        if l <= w or l <= h or l <= math.sqrt(math.pow(w, 2) + math.pow(h, 2)):
            print("DA")
        else:
            print("NE")

if __name__ == "__main__":
    main()