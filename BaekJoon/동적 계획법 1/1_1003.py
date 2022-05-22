# 피보나치 함수
import sys
input = sys.stdin.readline

t = int(input())

for test_case in range(t):
    num = int(input())

    count0 = 1
    count1 = 0

    for _ in range(num):
        temp = count1
        count1 += count0
        count0 = temp

    print(count0, count1)