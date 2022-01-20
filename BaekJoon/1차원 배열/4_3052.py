import sys

def main():
    num = []

    for i in range(10):
        n = int(sys.stdin.readline())
        num.append(n%42)

    num = list(dict.fromkeys(num))

    print(len(num))
    
if __name__ == "__main__":
    main()