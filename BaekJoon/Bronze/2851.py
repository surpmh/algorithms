# 슈퍼 마리오
import sys
input = sys.stdin.readline

mushroom = []
score = 0

for _ in range(10):
    mushroom.append(int(input()))

for i in mushroom:
    score += i

    if score >= 100:
        if score - 100 <= 100 - (score - i):
            print(score)
        else:
            print(score-i)
        break;