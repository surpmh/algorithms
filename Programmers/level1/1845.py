# 2016년
def solution(nums):
    n = len(nums) // 2
    nums = set(nums)
    
    if n< len(nums) :
        answer = n
    else:
        answer = len(nums)

    return answer

print(solution([3,1,2,3]))