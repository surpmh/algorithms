import math

def main():
    T = int(input())

    for Test_case in range(T):
        x1, y1, r1, x2, y2, r2 = map(int, input().split())

        d = math.sqrt(math.pow((x1 - x2), 2) + math.pow((y1 - y2), 2))

        if r1 < r2:
            r1, r2 = r2, r1

        if d == 0 and r1 == r2:
            result = -1
        elif r1 - r2 < d and r1 + r2 > d:
            result = 2
        elif r1 + r2 == d or r1 - r2 == d:
            result = 1
        elif r1 + r2 < d or r1 - r2 > d or (d == 0 and r1 != r2):
            result = 0
        
        print(result)

if __name__ == "__main__":
    main()