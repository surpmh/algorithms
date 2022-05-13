# [S/W 문제해결 기본] 1일차 - Flatten
def main():
    t = 10

    for test_case in range(t):
        result = 0
        n = int(input())
        box = list(map(int, input().split()))

        for i in range(n):
            max_index = box.index(max(box))
            min_index = box.index(min(box))

            box[max_index] -= 1
            box[min_index] += 1

        result = max(box) - min(box)

        print("#{0} {1}".format(test_case, result))

if __name__ == "__main__":
    main()