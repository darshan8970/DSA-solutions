# Piling Up!

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

There is a horizontal row of $n$ cubes. The length of each cube is given. You need to create a new vertical pile of cubes. The new pile should follow these directions: if $cube[i]$ is on top of $cube[j]$ then $sideLength[j]\ge sideLength[i]$. 

When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time. Print `Yes` if it is possible to stack the cubes. Otherwise, print `No`.  

**Example**   
$blocks = [1, 2, 3, 8, 7]$   

Result: `No`  

After choosing the rightmost element, $7$, choose the leftmost element, $1$.  After than, the choices are $2$ and $8$.  These are both larger than the top block of size $1$.

$blocks = [1, 2, 3, 7, 8]$   

Result: `Yes`

Choose blocks from right to left in order to successfully stack the blocks.   

**Input Format**

The first line contains a single integer $T$, the number of test cases.  
For each test case, there are $2$ lines.  
The first line of each test case contains $n$, the number of cubes.  
The second line contains $n$ space separated integers, denoting the *sideLengths* of each cube in that order.  



**Constraints**

$1\le T \le 5$  
$1\le n\le 10^5$  
$1\le sideLength < 2^{31}$

**Output Format**

For each test case, output a single line containing either `Yes` or `No`.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-10T17:30:42.110Z  

```py
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

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/piling-up/problem)