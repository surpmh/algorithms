# 좌표 압축
import sys

def main():
    n = int(sys.stdin.readline())
    x = list(map(int, sys.stdin.readline().split()))
    sort = sorted(set(x))
    dic = {sort[i]:i for i in range(len(sort))}

    for i in x:
        print(dic[i], end = ' ')

if __name__ == "__main__":
    main()