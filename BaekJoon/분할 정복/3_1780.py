# 종이의 개수
import sys
input = sys.stdin.readline

def part(x, y, n):
    check = p[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if p[i][j] != check:
                n //= 3
                part(x, y, n)
                part(x, y + n, n)
                part(x, y + (n * 2), n)
                part(x + n, y, n)
                part(x + n, y + n, n)
                part(x + n , y + (n * 2), n)
                part(x + (n * 2), y, n)
                part(x + (n * 2), y + n, n)
                part(x + (n * 2), y + (n * 2), n)
                return

    if check == -1:
        result[0] += 1
    elif check == 0:
        result[1] += 1
    else:
        result[2] += 1


n = int(input())
p = [list(map(int, input().split())) for _ in range(n)]
result = [0, 0, 0]

part(0, 0, n)

for cnt in result:
    print(cnt)