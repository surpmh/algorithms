# 파리 퇴치
def extermination(x, y):
    sum = 0
    for i in range(m):
        for j in range(m):
            sum += fly[y+i][x+j]

    return sum

T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    fly = [list(map(int, input().split())) for _ in range(n)]
    result = 0

    for i in range(n-m+1):
        for j in range(n-m+1):
            if extermination(j, i) >= result:
                result = extermination(j, i)

    print("#{0} {1}".format(test_case, result))