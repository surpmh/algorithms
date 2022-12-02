# 부분 문자열
import sys
input = sys.stdin.readline

s = input().rstrip()
p = input().rstrip()

print(1 if p in s else 0)