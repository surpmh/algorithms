# 점수 계산
import sys
input = sys.stdin.readline

score = []
final = []
total = 0

for _ in range(8):
    score.append(int(input()))

for i in range(5):
    final.append(sorted(score, reverse=True)[i])

print(sum(final))

for s in score:
    if s in final:
        print(score.index(s)+1, end=' ')
    else:
        continue