# 문서 검색
import sys
input = sys.stdin.readline

document = input().rstrip()
word = input().rstrip()

print(document.count(word))