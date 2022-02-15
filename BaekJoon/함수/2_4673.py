import sys

def solve(n):
    result = n
    
    while n:
        result += int(n % 10)
        n = int(n / 10)
        
    return result

def main():

    selfs = [True] * 10001

    for i in range(1, 10001):
        n = solve(i)
        if (n < 10001):
            selfs[solve(i)] = False

        if selfs[i]:
            print(i)

if __name__ == "__main__":
    main()