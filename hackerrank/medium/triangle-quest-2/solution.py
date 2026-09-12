for i in range(1, int(input()) + 1):
    print(sum(map(lambda x: x * 10 ** (x - 1) + x * 10 ** (2 * i - x - 1) if x != i else i * 10 ** (i - 1), range(1, i + 1))))
