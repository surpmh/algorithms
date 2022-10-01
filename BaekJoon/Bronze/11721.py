# 열 개씩 끊어 출력하기
import sys
input = sys.stdin.readline

str = input().rstrip()

for i in range(0, len(str), 10):
    print(str[i:i+10])