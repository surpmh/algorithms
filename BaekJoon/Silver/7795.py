# 먹을 것인가 먹힐 것인가
import sys
input = sys.stdin.readline

t = int(input())

for test_case in range(t):
    a, b = map(int, input().split())
    count = 0
    
    a_list = sorted(list(map(int, input().split())))
    b_list = sorted(list(map(int, input().split())))
    
    for i in a_list:
        start = 0
        end = b - 1
        pairs = -1
        while start <= end:
            mid = (start + end) // 2

            if b_list[mid] < i:
                pairs = mid
                start = mid + 1
            else:
                end = mid - 1

        count += pairs + 1
        
    print(count)