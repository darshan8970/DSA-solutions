# Tuples

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

**Task**  
Given an integer, $n$, and $n$ space-separated integers as input, create a tuple, $t$, of those $n$ integers. Then compute and print the result of $hash(t)$.  

**Note:** [hash()](https://docs.python.org/3/library/functions.html#hash) is one of the functions in the `__builtins__` module, so it need not be imported.  

**Input Format**

The first line contains an integer, $n$, denoting the number of elements in the tuple.	 			
The second line contains $n$ space-separated integers describing the elements in tuple $t$.  

**Constraints**

 

**Output Format**

Print the result of $hash(t)$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-03T14:40:02.754Z  

```py
if __name__ == '__main__':
    n = int(input())
    t = tuple(map(int, input().split()))

    # Reproduce the pre-Python-3.8 64-bit tuple hash algorithm
    mask = (1 << 64) - 1

    x = 0x345678
    mult = 1000003
    length = len(t)

    for item in t:
        y = hash(item)

        x = ((x ^ y) * mult) & mask

        length -= 1
        mult += 82520 + length + length
        mult &= mask

    x = (x + 97531) & mask

    # Convert unsigned 64-bit result to signed 64-bit integer
    if x >= (1 << 63):
        x -= (1 << 64)

    if x == -1:
        x = -2

    print(x)

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/python-tuples/problem)