def main():

    num = int(input())
    hive = 1
    count = 1

    while num > hive:
        hive += 6 * count
        count += 1
    
    print(count)

if __name__ == "__main__":
    main()