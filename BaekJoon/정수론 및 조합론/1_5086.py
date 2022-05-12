# 배수와 약수
import sys
input = sys.stdin.readline

def main():
    while True:
        a, b = map(int, input().split())
        if a + b == 0:
            break

        if a % b == 0:
            print("multiple")
        elif b % a == 0:
            print("factor")
        else:
            print("neither") 

if __name__ == "__main__":
    main()