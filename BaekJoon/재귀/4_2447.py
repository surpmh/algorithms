def star(n):
    for i in range(n):
        print()
        for j in range(n):
            if i == 1 and j % 3 == 1:
                print(" ", end='')
            else:
                print("*", end='')

    return(n//3)

def main():
    num = int(input())

    star(num)

if __name__ == "__main__":
    main()