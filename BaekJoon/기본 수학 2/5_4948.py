import math

def main():
    while True:
        n = int(input())
        m = 2*n

        if n == 0:
            break

        sieve = [True] * (m + 1)

        for i in range(2, int(math.sqrt(m)) + 1):
            if sieve[i] == True:
                for j in range(i+i, m+1, i):
                    sieve[j] = False

        list = [i for i in range(n+1, m+1) if sieve[i] == True]

        print(len(list))

if __name__ == "__main__":
    main()