# 간단한 369게임
def main():
    n = int(input())
    rule = [3, 6, 9]

    for i in range(1, n+1):
        num = list(map(int, str(i)))
        count = 0
        if rule[0] not in num and rule[1] not in num and rule[2] not in num:
            print(i, end=' ')
        else:
            for j in range(3):
                target = rule[j]  
                count += num.count(target)
            for _ in range(count):
                print('-', end='')
            print(end=' ')
    
if __name__ == "__main__":
    main()

# 다른 풀이
# def main():
#     n = int(input())
#     clap = ['3', '6', '9']

#     for i in range(1, n+1):
#         count = 0
#         for j in str(i):
#             if j in clap:
#                 count += 1
#         if count > 0:
#             i = "-" * count
#         print(i, end=' ')

# if __name__ == "__main__":
#     main()