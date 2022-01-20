import sys

def main():
    a = list(map(int, sys.stdin.readline().split()))

    print(min(a), max(a))

if __name__ == "__main__":
    main()