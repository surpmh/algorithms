import math

def main():
    R = int(input())
    
    print("{:.6f}".format(math.pi * R ** 2 ))
    print("{:.6f}".format(2 * R ** 2))

if __name__ == "__main__":
    main()