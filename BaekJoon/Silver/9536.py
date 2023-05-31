# 여우는 어떻게 울지?
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    sound = input().split()
    cry = []
    answer = []

    while True:
        call = list(map(str, input().split()))
        if call[0] == "what":
            break
        else:
            cry.append(call[2])

    for s in sound:
        if s not in cry:
            answer.append(s)

    print(' '.join(answer))