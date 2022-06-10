# [기초-종합] 수 나열하기2
a, r, n = map(int, input().split())
result = a * r

for i in range(n-2):
    result *= r

print(result)
