# 이중우선순위큐
import heapq

def solution(operations):
    max_heap = []
    min_heap = []

    for operation in operations:
        arr = list(map(str, operation.split()))
        if arr[0] == "I":
            heapq.heappush(min_heap, int(arr[1]))
            heapq.heappush(max_heap, -int(arr[1]))
        else:
            if arr[1] == "-1" and min_heap:
                heapq.heappop(min_heap)
                max_heap = []
                for heap in min_heap:
                    heapq.heappush(max_heap, -heap)
            elif arr[1] == "1" and max_heap:
                heapq.heappop(max_heap)
                min_heap = []
                for heap in max_heap:
                    heapq.heappush(min_heap, -heap)

    if max_heap:
        return [-heapq.heappop(max_heap), heapq.heappop(min_heap)]
    else:
        return [0, 0]
    
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))