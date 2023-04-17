# 호텔 대실
import heapq

def to_minute(time):
    h, m = map(int, time.split(":"))
    return h * 60 + m

def solution(book_time):
    room = []
    book_time.sort(key = lambda _:_[0])

    for time in book_time:
        start = to_minute(time[0])
        end = to_minute(time[1]) + 10

        if room and room[0] <= start:
            heapq.heappop(room)
        heapq.heappush(room, end)
            
    return len(room)

print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))