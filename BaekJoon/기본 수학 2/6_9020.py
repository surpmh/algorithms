import math

def prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def main():
    T = int(input())

    for test_case in range(T):
        num = int(input())

        for i in range(num // 2, -1, -1):
            if prime(i) and prime(num-i):
                print(i, num-i)
                break

if __name__ == "__main__":
    main()