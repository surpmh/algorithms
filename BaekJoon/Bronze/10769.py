# 행복한지 슬픈지
import sys
input = sys.stdin.readline

s = input().rstrip()

if ":-(" in s or ":-)" in s:
    if s.count(":-)") > s.count(":-("):
        print("happy")
    elif s.count(":-)") < s.count(":-("):
        print("sad")
    else:
        print("unsure")
else:
    print("none")