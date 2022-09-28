# UCPC는 무엇의 약자일까?
import sys
input = sys.stdin.readline

string = input().rstrip()
ucpc = ['U', 'C', 'P', 'C']
idx = 0

for i in string:
    if i == ucpc[idx]:
        idx += 1
    if idx == 4:
        break
    
if idx == 4:
    print("I love UCPC")
else:
    print("I hate UCPC")