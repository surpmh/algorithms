# 영화감독 숌
def main():
    end_num = '666'
    title = 666
    count = 0

    n = int(input())

    while True:
        if end_num in str(title):
            count += 1
        if count == n:
            print(title)
            break
        title += 1

if __name__ == "__main__":
    main()