# 패션왕 신해빈
import sys
from collections import Counter
input = sys.stdin.readline

def main():
    t = int(input())

    for test_case in range(t):
        n = int(input())
        case = []

        for _ in range(n):
            c, k = map(str, input().rstrip().split())
            case.append(k)

        num = 1
        result = Counter(case)
        
        for key in result:
            num *= result[key] +1

        print(num - 1)

if __name__ == "__main__":
    main()