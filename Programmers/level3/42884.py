# 단속 카메라
def solution(routes):
    answer = 1
    routes.sort(key=lambda x:x[1])

    for i in range(len(routes)):
        if i == 0:
            point = routes[i][1]
        else:
            if point < routes[i][0]:
                answer += 1
                point = routes[i][1]

    return answer

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))