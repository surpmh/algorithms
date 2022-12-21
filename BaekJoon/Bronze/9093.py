# 단어 뒤집기
import sys
input = sys.stdin.readline

t = int(input())

for test_case in range(t):
    s = input().rstrip()
    reverse = []

    for word in s.split():
        reverse.append(word[::-1] + " ")

    print(''.join(reverse))