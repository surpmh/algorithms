def main():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())

    x_list = x1, x2, x3
    y_list = y1, y2, y3

    for i in range(3):
        if x_list.count(x_list[i]) == 1:
            x = x_list[i]
        if y_list.count(y_list[i]) == 1:
            y = y_list[i]

    print(x, y)

if __name__ == "__main__":
    main()