import sys

def main():
    a = []
    
    for i in range(9):
        n = int(sys.stdin.readline())
        a.append(n)

    print(max(a))
    print(a.index(max(a))+1)

if __name__ == "__main__":
    main()