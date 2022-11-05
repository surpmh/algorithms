# 수학숙제
import sys
import re
input = sys.stdin.readline

n = int(input())
nums = []

for _ in range(n):
    s = input().rstrip()

    num = re.compile('[0-9]+')
    num = num.findall(s)

    for i in num:
        nums.append(int(i))

nums.sort()

for i in nums:
    print(i)