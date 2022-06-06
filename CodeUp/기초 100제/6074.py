# [기초-반복실행구조] 문자 1개 입력받아 알파벳 출력하기
a = ord(input())
b = ord('a')

while b <= a:
    print(chr(b), end=' ')
    b += 1