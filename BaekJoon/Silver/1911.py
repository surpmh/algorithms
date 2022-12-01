# 흙길 보수하기
import sys
input = sys.stdin.readline

n, l = map(int, input().split())
puddle = []
for _ in range(n):
    puddle.append(list(map(int, input().split())))

puddle.sort()
idx = 0
answer = 0

for start, end in puddle:
    idx = max(start, idx)

    count = ((end-idx) + l - 1) // l

    answer += count
    idx += count * l

print(answer)