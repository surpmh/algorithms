# 단어 정렬
import sys

def main():
    n = int(input())

    word = []

    for _ in range(n):
        word.append(sys.stdin.readline().strip())

    word = list(set(word))
    word.sort()
    word.sort(key = len)

    print('\n'.join(word))

if __name__ == "__main__":
    main()