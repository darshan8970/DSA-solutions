input()
n = list(map(int, input().split()))

set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))

print(sum((i in set_a) - (i in set_b) for i in n))
