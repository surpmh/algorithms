# 대칭 차집합
import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    a = set(sys.stdin.readline().split())
    b = set(sys.stdin.readline().split())  
    
    print(len(a - b) + len(b - a))

if __name__ == "__main__":
    main()