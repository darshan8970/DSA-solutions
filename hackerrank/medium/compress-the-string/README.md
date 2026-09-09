# Compress the String!

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

In this task, we would like for you to appreciate the usefulness of the _groupby()_ function of _itertools_ . To read more about this function, [Check this out](https://docs.python.org/2/library/itertools.html#itertools.groupby) .

You are given a string $S$. Suppose a character '$c$' occurs consecutively $X$ times in the string. Replace these consecutive occurrences of the character '$c$' with $(X,\;c)\;$ in the string. 

For a better understanding of the problem, check the explanation. 


**Input Format**

A single line of input consisting of the string $S$. 


**Output Format** 

A single line of output consisting of the modified string.

**Constraints**

All the characters of $S$ denote integers between $0$ and $9$. 

$1 \le \mid S \mid \le 10^{4}$

**Sample Input**

	1222311

**Sample Output**

	(1, 1) (3, 2) (1, 3) (2, 1)

**Explanation**

First, the character $1$ occurs only once. It is replaced by $(1,\;1)\;$. Then the character $2$ occurs three times, and it is replaced by $(3, \; 2)$ and so on. 

Also, note the single space within each compression and between the compressions. 



**Input Format**

 

**Output Format**

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-09T16:31:32.502Z  

```py
from itertools import groupby
string = input()
for k, v in groupby(string):
    print(f'({len(list(v))}, {k})', end=' ')

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/compress-the-string/problem)