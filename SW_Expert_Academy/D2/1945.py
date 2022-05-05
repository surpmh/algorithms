# 간단한 소인수분해
def main():
    T = int(input())

    for test_case in range(1, T + 1):
        num = int(input())
        a, b, c, d, e = 0, 0, 0, 0, 0

        while True:
            if num % 2 == 0:
                num /= 2
                a += 1
                continue
            elif num % 3 == 0:
                num /= 3
                b += 1
                continue
            elif num % 5 == 0:
                num /= 5
                c += 1
                continue
            elif num % 7 == 0:
                num /= 7
                d += 1
                continue
            elif num % 11 == 0:
                num /= 11
                e += 1
                continue
            else:
                break

        print("#{0}".format(test_case), a, b, c, d, e)

if __name__ == "__main__":
    main()