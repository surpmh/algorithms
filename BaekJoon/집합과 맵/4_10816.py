# 숫자 카드 2
import sys
from collections import Counter

def main():
    n = int(sys.stdin.readline())
    num_card = list(map(int, sys.stdin.readline().split()))

    m = int(sys.stdin.readline())
    sang_geun = list(map(int, sys.stdin.readline().split()))

    count = Counter(num_card)
    
    for i in range(len(sang_geun)):
        if sang_geun[i] in count:
            print(count[sang_geun[i]], end=' ')
        else:
            print(0, end=' ')

if __name__ == "__main__":
    main()