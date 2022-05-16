# 검문
import sys
import math
input = sys.stdin.readline

def main():
    t = int(input())
    n = list(int(input()) for _ in range(t))
    n.sort()
    temp = []
    m = set()

    for i in range(1, t):
        temp.append(n[i] - n[i-1])
        
    g = temp[0]
    for i in range(1, len(temp)):
        g = math.gcd(g, temp[i])

    for i in range(2, int(math.sqrt(g)) + 1):
        if g % i == 0:
            m.add(i)
            m.add(g // i)

    m.add(g)
    print(*sorted(list(m)))

if __name__ == "__main__":
    main()