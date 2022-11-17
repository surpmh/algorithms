# 게임
import sys
input = sys.stdin.readline

x, y = map(int, input().split())
z = y * 100 // x
answer = 0

if z >= 99:
    answer = -1
else:
    start = 1
    end = x

    while start <= end:
        mid = (start + end) // 2

        if (y + mid) * 100 // (x + mid) <= z:
            start = mid + 1
        else:
            answer = mid
            end = mid - 1

print(answer)