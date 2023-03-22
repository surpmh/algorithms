# 차이를 최대로
import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
answer = 0

for i in permutations(arr):
    sum = 0
    for j in range(n-1):
        sum += abs(i[j] - i[j+1])
    answer = max(answer, sum)

print(answer)