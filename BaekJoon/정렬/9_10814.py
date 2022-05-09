# 나이순 정렬
import sys

def main():
    n = int(input())
    member_list = []
    

    for _ in range(n):
        member_list.append(sys.stdin.readline().strip().split())

    member_list.sort(key=lambda member: int(member[0]))

    for member in member_list:
        print(*member, sep=' ')

if __name__ == "__main__":
    main()