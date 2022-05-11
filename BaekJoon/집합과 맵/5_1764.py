# 듣보잡
import sys
from collections import Counter

def main():
    n, m = map(int, sys.stdin.readline().split())
    people_list = []
    result = []

    for _ in range(n+m):
        people_list.append(*sys.stdin.readline().rstrip().split())
    
    people = Counter(people_list)

    for key, value in people.items():
        if value == 2:
            result.append(key)
    
    print(len(result))
    for i in sorted(result):
        print(i)
    
if __name__ == "__main__":
    main()