# 주식
import sys
input = sys.stdin.readline

t = int(input())

for test_case in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    sell = arr[-1]
    answer = 0

    for i in range(n-1, -1, -1):
        if sell < arr[i]:
            sell = arr[i]
        elif sell > arr[i]:
            answer += sell - arr[i]

    print(answer)