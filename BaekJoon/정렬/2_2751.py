# 수 정렬하기 2
import sys

def main():
    n = int(sys.stdin.readline())
    num = []

    for i in range(n):
        num.append(int(sys.stdin.readline()))

    for i in sorted(num):
        print(i)

if __name__ == "__main__":
    main()