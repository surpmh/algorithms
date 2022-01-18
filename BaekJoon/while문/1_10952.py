import sys

def main():
    while True:
        a, b = map(int, sys.stdin.readline().split())
        if a == 0 and b == 0:
            break
        print(a + b)

if __name__ == "__main__":
    main()