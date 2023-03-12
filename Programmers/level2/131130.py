# 혼자 놀기의 달인
def solution(cards):
    box = []
    visited = [False] * len(cards)

    for i in range(1, len(cards)+1):
        if not visited[i-1]:
            box.append(dfs(cards, visited, i, 0))

    box.sort(reverse=True)

    if len(box) < 2:
        return 0
    else:
        return box[0] * box[1]
    
def dfs(cards, visited, idx, count):
    if visited[idx-1]:
        return count
    
    visited[idx-1] = True
    return dfs(cards, visited, cards[idx-1], count+1)

print(solution([ 2, 3, 4, 5, 6, 7, 8, 9, 10 , 1 ]))