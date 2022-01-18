def main():
    n = int(input())
    num = n
    count = 0

    while True:
        if n < 10:
            n1 = 0
            n2 = n
        else:
            n1 = n // 10
            n2 = n % 10
        
        n3 = (n1 + n2) % 10
        n = n2*10+n3
        count += 1

        if n == num:
            print(count)
            break

if __name__ == "__main__":
    main()