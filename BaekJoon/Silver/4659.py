# 비밀번호 발음하기
import sys
import re
input = sys.stdin.readline

while True:
    s = input().rstrip()

    if s == "end":
        break

    case1 = len(re.findall('[aeiou]',s)) != 0
    case2 = len(re.findall('[aeiou]{3}|[^aeiou]{3}',s)) == 0
    case3 = len(re.findall('([a-df-np-z])\\1',s)) == 0

    if case1 and case2 and case3:
        print("<" + s + "> is acceptable.")
    else:
        print("<" + s + "> is not acceptable.")