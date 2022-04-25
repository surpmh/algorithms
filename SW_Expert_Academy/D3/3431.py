T = int(input())

for test_case in range(1, T+1):
    L, U, X = map(int, input().split())
    if X > U:
        print("#{0} -1".format(test_case))
    elif X >= L and X <= U:
        print("#{0} 0".format(test_case))
    else:
        print("#{0} {1}".format(test_case, L-X))