# 백만 장자 프로젝트
import queue

def main():
    T = int(input())

    for test_case in range(1, T + 1):
        n = int(input())
        price = list(map(int, input().split()))
        price.reverse()
        maxnum = price[0]
        result = 0

        for i in range(n):
            if maxnum > price[i]:
                result += maxnum - price[i]
            else:
                maxnum = price[i]

        print("#{0} {1}".format(test_case, result))

if __name__ == "__main__":
    main()