# 명예의 전당 (1)
import heapq

def solution(k, score):
    answer = []
    heap = []
    
    for s in score:
        if not heap or len(heap) <= k or heap[0] <= s:
            heapq.heappush(heap, s)

        if len(heap) > k:
            heapq.heappop(heap)

        answer.append(heap[0])
        
    return answer

print(solution(3, [10, 100, 20, 150, 1, 100, 200]))