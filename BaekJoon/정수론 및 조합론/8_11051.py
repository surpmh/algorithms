# 이항 계수 2
import sys
input = sys.stdin.readline

def main():
    n, k = map(int, input().split())
    li = [[0 for i in range(1001)] for j in range(1001)]
    li[0][0] = li[1][0] = li[1][1] = 1
    
    for i in range(2, 1001):
        for j in range(i+1):
            if j == 0 or i == j:
                li[i][j] = 1
            else:
                li[i][j] = li[i-1][j-1] + li[i-1][j]

    print(li[n][k] % 10007)

if __name__ == "__main__":
    main()