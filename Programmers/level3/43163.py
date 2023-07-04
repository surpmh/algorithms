# 단어 변환
answers = []

def dfs(begin, target, words, visited, depth):
    if begin == target:
        answers.append(depth)
    
    for i in range(len(words)):
        diff = 0
        for j in range(len(begin)):
            if words[i][j] != begin[j]:
                diff += 1
        if not visited[i] and diff == 1:
            visited[i] = 1
            dfs(words[i], target, words, visited, depth+1)
            visited[i] = 0

    return answers
    
def solution(begin, target, words):
    if target not in words:
        return 0
    
    visited = [0] * len(words)
    
    dfs(begin, target, words, visited, 0)

    return min(answers)

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))