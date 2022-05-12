# 약수
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    a = list(map(int, input().split()))

    print(max(a) * min(a))

if __name__ == "__main__":
    main()