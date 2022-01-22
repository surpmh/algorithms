import sys

def main():
    c = int(sys.stdin.readline())

    for i in range(c):
        score = list(map(int, sys.stdin.readline().split()))

        avg = (sum(score)-score[0]) / (len(score)-1)

        count = 0

        for i in range(1, len(score)):
            if score[i] > avg:
                count += 1

        result = '%.3f' % (count/score[0]*100)
            
        print('{}%'.format(result))

if __name__ == "__main__":
    main()