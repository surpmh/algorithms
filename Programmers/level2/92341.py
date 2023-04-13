# 주차 요금 계산
import math

def solution(fees, records):
    answer = {}
    car = {}

    for record in records:
        time, num, state = record.split()
        if state == "IN":
            h, m = map(int, time.split(":"))
            car[num] = h * 60 + m
        else:
            h, m = map(int, time.split(":"))
            minute = (h * 60 + m) - car[num]
            
            if num in answer:
                answer[num] += minute
            else:
                answer[num] = minute

            del car[num]

    for key, value in car.items():
        minute = (23 * 60 + 59) - value

        if key in answer:
            answer[key] += minute
        else:
            answer[key] = minute

    return [fees[1] + math.ceil(max(0, (minute - fees[0])) / fees[2]) * fees[3] for key, minute in sorted(answer.items(), key=lambda x :x[0])]

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))