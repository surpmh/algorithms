# 달팽이 숫자
def main():
    T = int(input())

    for test_case in range(1, T + 1):
        n = int(input())
        snail = [[0] * n for _ in range(n)]

        row = 0
        col = -1
        cnt = 1
        trans = 1

        while n > 0:
            for _ in range(n):
                col += trans
                snail[row][col] = cnt
                cnt += 1
            n -= 1
            for _ in range(n):
                row += trans
                snail[row][col] = cnt
                cnt += 1
            trans *= -1

        print("#{0}".format(test_case))
        
        for i in snail:
            print(*i)

if __name__ == "__main__":
    main()