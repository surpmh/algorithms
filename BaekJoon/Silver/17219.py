# 비밀번호 찾기
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dict = {}
start = 0
end = n

for _ in range(n):
    domain, passwd = map(str, input().rstrip().split())

    dict[domain] = passwd

for _ in range(m):
    search = input().rstrip()
    print(dict[search])