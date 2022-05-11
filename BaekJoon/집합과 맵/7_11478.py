# 서로 다른 부분 문자열의 개수
import sys

def main():
    string = sys.stdin.readline().rstrip()
    result = set()

    for i in range(len(string)+1):
        for j in range(i+1, len(string)+1):
            result.add(string[i:j])

    print(len(result))

if __name__ == "__main__":
    main()