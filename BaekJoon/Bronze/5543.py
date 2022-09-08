# 상근날드
import sys
input = sys.stdin.readline

menu = []

for _ in range(5):
    menu.append(int(input()))

print(min(menu[0]+menu[3], menu[1]+menu[3], menu[2]+menu[3], menu[0]+menu[4], menu[1]+menu[4], menu[2]+menu[4])-50)