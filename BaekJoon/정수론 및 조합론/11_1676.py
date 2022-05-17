# 팩토리얼 0의 개수
import sys
import math
input = sys.stdin.readline

def main():
    n = int(input())
    result = 0

    n = math.factorial(n)
    n = str(n)

    for i in range(1, len(n)+1):
        if n[-i] == '0':
            result += 1
        else:
            break

    print(result)

if __name__ == "__main__":
    main()