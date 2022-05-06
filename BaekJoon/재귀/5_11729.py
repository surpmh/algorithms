def hanoi(num, start, by, to):
    if num == 1:
        print(start, to)
    else:
        hanoi(num - 1, start, to, by)
        print(start, to)
        hanoi(num - 1, by, start, to)

def main():
    n = int(input())

    print(2**n-1)
    hanoi(n, 1, 2, 3)

if __name__ == "__main__":
    main()