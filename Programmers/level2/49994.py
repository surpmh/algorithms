# 방문 길이
def solution(dirs):
    answer = 0
    move = {'U': [0, 1], 'D': [0, -1], 'R': [1, 0], 'L': [-1, 0]}
    visited = []
    location = [0, 0]

    for i in dirs:
        way = [location]
        if -5 <= location[0] + move[i][0] <= 5 and -5 <= location[1] + move[i][1] <= 5:
            location = [x + y for x, y in zip(location, move[i])]
            way.append(location)
        
            if way not in visited and [way[1], way[0]] not in visited:
                visited.append(way)
                answer += 1

    return answer

print(solution("ULURRDLLU"))