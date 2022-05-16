# 농작물 수확하기
def main():
    t = int(input())

    for test_case in range(1, t+1):
        sum = 0
        farm = []
        n = int(input())

        [farm.append(list(map(str, input()))) for _ in range(n)]    

        for i in range(n):
            if i <= n // 2:
                l = i
            else:
                l -= 1
            for j in range(n // 2 - l, n // 2 + l + 1):
                sum += int(farm[i][j])

        print("#{0} {1}".format(test_case, sum))

if __name__ == "__main__":
    main()