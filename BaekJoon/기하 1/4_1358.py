# 하키
import sys
import math
input = sys.stdin.readline

def main():
    count = 0
    w, h, x, y, p = map(int, input().split())
    r = h/2

    for _ in range(p):
        xp, yp = map(int, input().split())

        d1 = math.sqrt(math.pow(xp - x, 2) + math.pow(yp - (y + r), 2))
        d2 = math.sqrt(math.pow(xp - (x + w), 2) + math.pow(yp - (y + r), 2))

        if ((xp >= x and xp <= x + w) and (yp >= y and yp <= y + h)) or d1 <= r or d2 <= r:
            count += 1

    print(count)

if __name__ == "__main__":
    main()