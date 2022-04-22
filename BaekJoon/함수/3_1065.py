import sys

def solve(n):
    result = 0

    if len(str(n)) <= 2:
        result = n
    else:
        result = 99
        for i in range(100, n+1):
            if (int(str(i)[0]) - int(str(i)[1])) == (int(str(i)[1]) - int(str(i)[2])):
                result += 1

    return result

def main():
    num = int(sys.stdin.readline())

    print(solve(num))

if __name__ == "__main__":
    main()