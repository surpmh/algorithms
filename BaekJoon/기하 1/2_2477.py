# 참외밭
import sys
input = sys.stdin.readline

def main():
    k = int(input())
    max_width = 0
    max_height = 0
    width_index = 0
    height_index = 0
    field = [list(map(int, input().split())) for _ in range(6)]

    for i in range(len(field)):
        if field[i][0] == 1 or field[i][0] == 2:
            if max_width < field[i][1]:
                max_width = field[i][1]
                width_index = i
        else:
            if max_height < field[i][1]:
                max_height = field[i][1]
                height_index = i
    
    min_width = abs(field[(width_index-1) % 6][1] - field[(width_index+1) % 6][1])
    min_height = abs(field[(height_index-1) % 6][1] - field[(height_index+1) % 6][1])
    area = (max_width*max_height) - (min_width*min_height)

    print(k*area)

if __name__ == "__main__":
    main()