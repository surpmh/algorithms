# 만능 오라클
import sys
input = sys.stdin.readline

strings = input().rstrip().split("What is")

for string in strings[1:]:
    if "?" in string:
        if "." in string[:string.index("?")]:
            continue
        else:
            print("Forty-two is" + string[:string.index("?")] + ".")