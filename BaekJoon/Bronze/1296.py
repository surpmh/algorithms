# 팀 이름 정하기
import sys
input = sys.stdin.readline

yd = input().rstrip()
n = int(input())
list = []
for _ in range(n):
    name = input().rstrip()

    s = yd + name
    L = s.count("L")
    O = s.count("O")
    V = s.count("V")
    E = s.count("E")
    num = ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100
    list.append((num, name))
    
list.sort(key=lambda x : (-x[0], x[1]))

print(list[0][1])