import sys

def main():
    t = int(sys.stdin.readline())

    for i in range(1, t+1):
        result = 0
        for n in list(map(int, sys.stdin.readline().split())):
            if n % 2 == 1:
                result += n
        print(f"#{i} {result}")

if __name__ == "__main__":
    main()