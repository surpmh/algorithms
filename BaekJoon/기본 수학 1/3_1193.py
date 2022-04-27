def main():

    x, y = 1, 1

    num = int(input())
    
    index = 1

    while True:
        if index * (index + 1) // 2 >= num:
            break
        else:
            index += 1

    n = num - (index * (index - 1) // 2)

    if index % 2 == 0:
        trans = 1
        x = 0
        y = index + 1
    else:
        trans = -1
        x = index + 1
        y = 0

    for j in range(n):
        x += trans
        y -= trans

    index += 1
            
    print("{0}/{1}".format(x, y))

if __name__ == "__main__":
    main()