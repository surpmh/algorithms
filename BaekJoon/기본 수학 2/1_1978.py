def main():
    N = int(input())
    count = 0
    
    num_list = list(map(int, input().split()))

    for test_case in range(len(num_list)):
        if num_list[test_case] == 1:
            count += 1
        i = 2
        while i < num_list[test_case]:
            if num_list[test_case] % i == 0:
                count += 1
                break
            else:
                i += 1
    
    print(N - count)

if __name__ == "__main__":
    main()