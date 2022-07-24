# 과제 안 내신 분..?
import sys
input = sys.stdin.readline

arr = list(range(1, 31))

for _ in range(28):
    arr.remove(int(input()))

for n in arr:
    print(n)