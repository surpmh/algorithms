# 일곱 난쟁이
import sys
input = sys.stdin.readline

def dfs(start):
    if len(dwarfs) == 7 and sum(dwarfs) == 100:
        dwarfs.sort()
        for dwarf in dwarfs:
            print(dwarf)
        exit()
            
    for i in range(start, 9):
        if not visited[i]:
            dwarfs.append(arr[i])
            visited[i] = True
            dfs(i)
            visited[i] = False
            dwarfs.pop()
            
arr = []

for i in range(9):
    arr.append(int(input()))
    
visited = [False for _ in range(9)]
dwarfs = []

dfs(0)