# [S/W 문제해결 기본] 1일차 - 최빈수 구하기
from collections import Counter

def main():
    T = int(input())

    for test_case in range(1, T + 1):
        n = int(input())
        arr = list(map(int, input().split()))

        result = Counter(arr).most_common()[0][0]

        print("#{0} {1}".format(test_case, result))

if __name__ == "__main__":
    main()
