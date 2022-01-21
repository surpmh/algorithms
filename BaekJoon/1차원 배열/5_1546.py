import sys

def main():
    n = int(sys.stdin.readline())
    
    score = list(map(int, sys.stdin.readline().split()))

    newscore = [score[i] / max(score) * 100 for i in range(len(score))]

    scoreavg = sum(newscore) / len(newscore)

    print(scoreavg)

if __name__ == "__main__":
    main()