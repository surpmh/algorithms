import math

def main():
    M, N = map(int, input().split())
    if M == 1:
        M += 1
    sieve = [True] * (N + 1)

    for i in range(2, int(math.sqrt(N)) + 1):
        if sieve[i] == True:
            for j in range(i+i, N+1, i):
                sieve[j] = False

    list = [i for i in range(M, N+1) if sieve[i] == True]

    print(*list, sep='\n')

if __name__ == "__main__":
    main()