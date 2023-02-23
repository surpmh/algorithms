# 대충 만든 자판
def solution(keymap, targets):
    answer = []
    
    for target in targets:
        count = 0
        for i in target:
            idx = []
            for map in keymap:
                if i in map:
                    idx.append(map.index(i) + 1)

            if idx:
                count += min(idx)
            else:
                count = -1
                
        answer.append(count)

    return answer

print(solution(["ABACD", "AF", "BCEFD"], ["ABCD", "AG", "AABB"]))