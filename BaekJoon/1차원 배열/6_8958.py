import sys

def main():
    n = int(sys.stdin.readline())

    for i in range(n):
        ox = list(sys.stdin.readline())

        count = 0
        score = 0

        for i in range(len(ox)):
            if ox[i] == 'O':
                count += 1
                score += count
            else:
                count = 0
        
        print(score)

if __name__ == "__main__":
    main()