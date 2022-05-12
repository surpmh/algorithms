# [S/W 문제해결 기본] 1일차 - View
def main():
    t = int(input())

    for test_case in range(t):
        count = 0
        n = int(input())
        building = list(map(int, input().split()))

        for i in range(2, n - 2):
            h = [(building[j]) for j in range(i-2, i+3)]

            if max(h) == h[2]:
                sort = sorted(h, reverse=True)
                count += sort[0] - sort[1]

        print("#{0} {1}".format(test_case, count))

if __name__ == "__main__":
    main()