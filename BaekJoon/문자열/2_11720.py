import sys

T = input()
num = input()
result = 0

for i in range(len(num)):
    n = int(str(num)[i])
    result += n

print(result)
