# 별 찍기 - 10
def draw_star(n) :
    if n == 1:
        return ['*']
    stars = draw_star(n//3)
    canvus = []

    for star in stars:
        canvus.append(star*3)
    for star in stars:
        canvus.append(star + ' ' * (n // 3) + star)
    for star in stars:
        canvus.append(star*3)

    return canvus
    
def main():
    num = int(input())

    print('\n'.join(draw_star(num)))
if __name__ == "__main__":
    main()