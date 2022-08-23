# 기타줄
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
    
price = []
p = []
o = []

for _ in range(m):
    package, one = map(int, input().split())

    p.append(package)
    o.append(one)

pp = min(p)
op = min(o)

if n <= 6:
    price.append(min(pp, op*n))
elif n >= 6 and n % 6 == 0:
    price.append(min(pp * (n // 6), op * (n)))
else:
    price.append(min(pp * ((n // 6) + 1), (pp * (n // 6)) + (op * (n % 6)), op * (n)))

print(min(price))