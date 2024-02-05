def solution(bandage, health, attacks):
    max_health = health
    time = 0
    idx = 0
    
    for i in range(attacks[-1][0] + 1):
        if i == attacks[idx][0]:
            health -= attacks[idx][1]
            
            if health <= 0:
                return -1
            
            idx += 1
            time = 0
        else:
            time += 1
            health += bandage[1]
            
            if time == bandage[0]:
                health += bandage[2]
                time = 0
            
            health = min(max_health, health)
        
    return health

print(solution([5, 1, 5], 30, [[2, 10], [9, 15], [10, 5], [11, 5]]))