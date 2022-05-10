# 문자열 집합
import sys

def main():
    count = 0
    n, m = map(int, sys.stdin.readline().split())
    s = set([sys.stdin.readline().strip() for _ in range(n)])

    for i in range(m):
        t = sys.stdin.readline().strip()
        if t in s:
            count += 1

    print(count)

if __name__ == "__main__":
    main()