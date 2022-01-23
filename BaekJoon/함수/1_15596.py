import sys

def solve(a):

    result = sum(a)

    return result

def main():

    n = list(map(int, sys.stdin.readline().split()))

    print(solve(n))


if __name__ == "__main__":
    main()


# def solve(a):
#     ans = 0
#     return ans