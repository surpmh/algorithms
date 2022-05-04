# 덩치
def main():
    n = int(input())
    bulk = []

    for i in range(n):
        bulk.append(list(map(int, input().split())))

    for i in range(n):
        rank = 1
        for j in range(n):
            if i == j:
                continue
            if bulk[i][0] < bulk[j][0] and bulk[i][1] < bulk[j][1]:
                rank += 1
        
        print(rank, end=' ')

if __name__ == "__main__":
    main()