# 핸드폰 번호 궁합
import sys
input = sys.stdin.readline

a = list(map(int, input().rstrip()))
b = list(map(int, input().rstrip()))
arr = [0]*16

for i in range(16):
    if i % 2 == 0:
        arr[i] = a[i // 2]
    else:
        arr[i] = b[i // 2]


while len(arr) != 2:
    temp = []
    for i in range(len(arr)-1):
        num = (arr[i] + arr[i+1]) % 10
        temp.append(num)
    arr = temp

print(*arr, sep="")