# 기상청 인턴 신현수
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
temp = list(map(int, input().split()))
d_sum = []

for i in range(n-k+1):
    d_sum.append(sum(temp[i:i+k]))

print(max(d_sum))