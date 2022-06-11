# 음계
import sys
input = sys.stdin.readline

s = list(map(int, input().split()))

if s == sorted(s):
    print("ascending")
elif s == sorted(s, reverse=True):
    print("descending")
else:
    print("mixed")