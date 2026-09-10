from collections import deque

T = int(input())
for _ in range(T):
    n = int(input())
    d = deque(list(map(int, input().split())))
    prev = float('inf')
    while d:
        if d[0] >= d[-1]:
            current = d.popleft()
        else:
            current = d.pop()
            
        if current > prev:
            print("No")
            break
        prev = current
    else:
        print('Yes')
