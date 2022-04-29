def main():
    T = int(input())

    for test_case in range(T):
        k = int(input())
        n = int(input())

        floor = [x for x in range(1, n+1)]

        for i in range(k):
            for j in range(1, n):
                floor[j] += floor[j-1]

        print(floor[-1])

if __name__ == "__main__":
    main()