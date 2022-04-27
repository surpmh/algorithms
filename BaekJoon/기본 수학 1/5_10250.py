import math

def main():

    T = int(input())

    for test_case in range(T):
        H, W, N = map(int, input().split())

        floor = N % H
        num = math.ceil(float(N) / H)

        if floor == 0:
            floor = H


        print('{}{:02d}'.format(floor, num))

if __name__ == "__main__":
    main()