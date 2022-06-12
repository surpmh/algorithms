# [기초-리스트] 성실한 개미
box = [list(map(int, input().split())) for _ in range(10)]

def dfs(x, y):
    if box[y][x] == 2 or (x == 8 and y == 8):
        box[y][x] = 9
        return
    if box[y][x] == 0:
        box[y][x] = 9
        if box[y][x+1] != 1:
            dfs(x+1, y)
        else:
            dfs(x, y+1)

dfs(1, 1)

for i in box:
    print(*i)