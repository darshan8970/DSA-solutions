if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
    records = sorted(records)
    scores = sorted(set(
        [records[i][1] for i in range(len(records))]))
    secondlowest = scores[1]
    for i in range(len(records)):
        if records[i][1] == secondlowest:
            print(records[i][0])
