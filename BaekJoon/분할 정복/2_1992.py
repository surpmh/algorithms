# 쿼드트리
import sys
input = sys.stdin.readline

def part(x, y, n):
    color = p[x][y]
    
    for i in range(x, x+n):
        for j in range(y, y+n):
            if p[i][j] != color:
                print('(', end='')
                part(x, y, n//2)
                part(x, y + n // 2, n // 2)
                part(x + n // 2, y, n // 2)           
                part(x + n // 2, y + n // 2, n // 2)
                print(')', end='')
                return

    if color == '0':
        print(0, end='')
    else:
        print(1, end='')

n = int(input())
p = [str(input()) for _ in range(n)]

part(0, 0, n)