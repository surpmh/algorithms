#import sys

def main():
    a = int(input())
    b = int(input())
    c = int(input())

    num = a * b * c
    
    n = list(str(num))
    
    for i in range(10):
        print(n.count(str(i)))

if __name__ == "__main__":
    main()