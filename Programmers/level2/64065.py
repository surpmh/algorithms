# 튜플
def solution(s):
    s = ''.join(s[1:-1].split('{')).split('}')[:-1]
    dict = {}

    for i in s:
        nums = i.split(',')

        for num in nums:
            if num:
                if num in dict:
                    dict[num] += 1
                else:
                    dict[num] = 1

    return [int(k) for k, v in sorted(dict.items(), key=lambda x: x[1], reverse=True)]

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))