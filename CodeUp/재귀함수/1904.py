# 두 수 사이의 홀수 출력하기
import sys
input = sys.stdin.readline

def recursion(a, b):
    if a > b:
        return

    if a % 2 == 1:
        print(a, end=' ')
    recursion(a + 1, b)

num1, num2 = map(int, input().split())

recursion(num1, num2)