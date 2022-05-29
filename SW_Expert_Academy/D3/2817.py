# 부분 수열의 합
from itertools import combinations
def main():
    T = int(input())

    for test_case in range(1, T+1):
        n, k = map(int, input().split())
        s = list(map(int, input().split()))
        result = 0

        for i in range(1, n+1):
            for value in combinations(s, i):
                if sum(value) == k:
                    result += 1

        print("#{0} {1}".format(test_case, result))

if __name__ == "__main__":
    main()