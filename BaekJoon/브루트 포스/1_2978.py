# 블랙잭
def main():
    n, m = map(int, input().split())
    number = list(map(int, input().split()))

    min = 100000
    
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                sum = number[i] + number[j] + number[k]
                sub = m - sum
                if sum <= m and sub <= min:
                    result = sum
                    min = sub

    print(result)

if __name__ == "__main__":
    main()