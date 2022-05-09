# 소트인사이드
import sys

def main():
    num = list(map(int, sys.stdin.readline().rstrip()))
    num.sort(reverse=True)

    for i in num:
        print(i, end='')

if __name__ == "__main__":
    main()