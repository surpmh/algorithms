# 3의 배수
import sys
input = sys.stdin.readline

def y(x):
    global count
    sum = 0
    if len(x) == 1:
        print(count)
        print("NO" if int(x) % 3 else "YES")
    else:
        count += 1
        for n in x:
            sum += int(n)
        return y(str(sum))

x = input().rstrip()
count = 0

y(x)