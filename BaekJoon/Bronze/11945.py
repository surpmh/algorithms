# 뜨거운 붕어빵
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
fish = []

for _ in range(n):
    fish.append(list(map(str, input().rstrip())))

for i in range(n):
    print(''.join(list(map(str, reversed(fish[i])))))