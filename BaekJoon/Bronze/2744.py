# 대소문자 바꾸기
import sys
input = sys.stdin.readline

word = input().rstrip()

for s in word:
    if s.isupper() == True:
        print(s.lower(), end='')
    else:
        print(s.upper(), end='')