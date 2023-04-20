# 모든 순열
import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
nums = [i for i in range(1, n+1)]
permutation_list = list(permutations(nums))

for permutation in permutation_list:
    print(' '.join(map(str, permutation)))