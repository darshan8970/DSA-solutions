from collections import defaultdict
x = input()
d = defaultdict(list)
for i in range(0, int(x)):
    d[input()].append(i)
print(len(d))
print(*list(len(values) for key, values in d.items()))
