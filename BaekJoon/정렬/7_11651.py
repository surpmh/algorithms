# 좌표 정렬하기 2
import sys

def main():
    n = int(sys.stdin.readline())
    coordinate = []

    for _ in range(n):
        x, y = map(int, sys.stdin.readline().split())
        coordinate.append([y, x])
    
    coordinate.sort()

    for y, x in coordinate:
        print(x, y)

if __name__ == "__main__":
    main()