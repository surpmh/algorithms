# 베스트셀러
import sys
input = sys.stdin.readline

n = int(input())
dict = {}

for _ in range(n):
    book = input()

    if book in dict:
        dict[book] += 1
    else:
        dict[book] = 1

val = max(dict.values())

best = []

for book, count in dict.items():
    if count == val:
        best.append(book)

print(sorted(best)[0], end='')