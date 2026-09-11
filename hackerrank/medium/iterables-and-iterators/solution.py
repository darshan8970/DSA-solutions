from itertools import combinations
from math import comb

# parameters
n = int(input())
letters = "".join(input().split())[:n]
k = int(input())

# total combinations and count 'a's
tot = comb(n, k)
cnt = sum('a' in i for i in combinations(letters, k))

#result with 3 decimal places
print(f'{(cnt/tot):.3f}')
