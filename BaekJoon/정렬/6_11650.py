# 좌표 정렬하기
import sys

def main():
    n = int(sys.stdin.readline())
    coordinate = []

    for _ in range(n):
        coordinate.append(list(map(int, sys.stdin.readline().strip().split())))

    coordinate.sort()

    for i in range(n):
        print(*coordinate[i])

if __name__ == "__main__":
    main()