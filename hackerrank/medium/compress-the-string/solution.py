from itertools import groupby
string = input()
for k, v in groupby(string):
    print(f'({len(list(v))}, {k})', end=' ')
