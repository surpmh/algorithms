# 공 넣기
import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    arr = [0] * (n + 1)

    for _ in range(m):
        i, j, k = map(int, input().split())
        for n in range(i, j+1):
            arr[n] = k

    del arr[0]

    print(*arr)

if __name__ == "__main__":
    main()