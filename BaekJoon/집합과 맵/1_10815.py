# 숫자 카드
import sys

def main():
    n = int(sys.stdin.readline())
    num_card = set(map(int, sys.stdin.readline().split()))

    m = int(sys.stdin.readline())
    sang_geun = list(map(int, sys.stdin.readline().split()))

    for i in range(m):
        if sang_geun[i] in num_card:
            print(1, end=' ')
        else:
            print(0, end=' ')

if __name__ == "__main__":
    main()