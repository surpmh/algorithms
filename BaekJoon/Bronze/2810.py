# 컵홀더
import sys
input = sys.stdin.readline

n = int(input())
seat = input().rstrip()
count = seat.count('LL')

if (count <= 1):
    print(len(seat))

else:
    print(len(seat) - count + 1)