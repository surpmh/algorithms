# 나는야 포켓몬 마스터 이다솜
import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    book = {}

    for i in range(1, n+1):
        pokemon = sys.stdin.readline().rstrip()
        book[i] = pokemon
        book[pokemon] = i

    for _ in range(m):
        quest = sys.stdin.readline().rstrip()

        if quest.isdigit():
            print(book[int(quest)])
        else:
            print(book[quest])  

if __name__ == "__main__":
    main()