if __name__ == '__main__':
    N = int(input())
    command = []
    res = []
    for _ in range(N):
        command.append(input().split())
    for i in command:
        if i[0] == "insert":
            res.insert(int(i[1]), int(i[2]))
        elif i[0] == "append":
            res.append(int(i[1]))
        elif i[0] == "print":
            print(res)
        elif i[0] == "remove":
            res.remove(int(i[1]))
        elif i[0] == "sort":
            res.sort()
        elif i[0] == "pop":
            res.pop(-1)
        elif i[0] == "reverse":
            res.reverse()
