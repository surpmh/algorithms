# 색종이 만들기
import sys
input = sys.stdin.readline

def part(x, y, n):
    global white
    global blue

    color = p[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if p[i][j] != color:
                part(x, y, n//2)
                part(x, y + n // 2, n // 2)
                part(x + n // 2, y, n // 2)           
                part(x + n // 2, y + n // 2, n // 2)
                return

    if color == 0:
        white += 1
    else:
        blue += 1

n = int(input())
p = [list(map(int, input().split())) for _ in range(n)]

white = 0
blue = 0

part(0, 0, n)

print(white)
print(blue)