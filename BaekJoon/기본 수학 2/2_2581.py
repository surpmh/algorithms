def main():
    M = int(input())
    N = int(input())
    sum, sosu = 0, 0

    for i in range(N, M-1, -1):
        if i == 1:
            continue
        if i == 2:
            sosu = i
            sum += sosu
        for j in range(2, i):
            if i % j == 0:
                break
            if j == i-1:
                sosu = i
                sum += sosu

    if sum == 0:
        print(-1)
    else:
        print(sum)
        print(sosu)

if __name__ == "__main__":
    main()