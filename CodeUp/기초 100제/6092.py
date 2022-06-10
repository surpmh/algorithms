# [기초-리스트] 이상한 출석 번호 부르기1
n = int(input())
count = list(map(int, input().split()))
result = [0] * 23

for i in range(n):
    result[count[i]-1] += 1

print(*result)