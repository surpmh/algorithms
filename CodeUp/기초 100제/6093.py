# [기초-리스트] 이상한 출석 번호 부르기2
n = int(input())
arr = list(map(int, input().split()))

print(*list(reversed(arr)))