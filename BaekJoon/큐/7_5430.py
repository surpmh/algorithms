# AC
import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    ad = input().rstrip()
    n = int(input())
    q = deque(input().rstrip()[1:-1].split(','))
    count = 0
    flag = False

    if n == 0:
        q = deque()

    for str in ad:
        if str == 'R':
            count += 1
        else:
            if q:
                if count % 2 == 0:
                    q.popleft()
                else:
                    q.pop()
            else:
                flag = True
                print("error")
                break

    if not flag:
        if count % 2 == 0:
            print("[" + ",".join(q) + "]")
        else:
            q.reverse()
            print("[" + ",".join(q) + "]")