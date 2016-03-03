# 006: Maximum path sum

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23 (3 + 7 + 4 + 9).

<p align="center">
   <strong>3</strong><br>
  <strong>7</strong> 4<br>
 2 <strong>4</strong> 6<br>
8 5 <strong>9</strong> 3
</p>

Find the maximum total from top to bottom of the triangle below:

<p align="center">
75<br>
95 64<br>
17 47 82<br>
18 35 87 10<br>
20 04 82 47 65<br>
19 01 23 75 03 34<br>
88 02 77 73 07 63 67<br>
99 65 04 28 06 16 70 92<br>
41 41 26 56 83 40 80 70 33<br>
41 48 72 33 47 32 37 16 94 29<br>
53 71 44 65 25 43 91 52 97 51 14<br>
70 11 33 28 77 73 17 78 39 68 17 57<br>
91 71 52 38 17 14 91 43 58 50 27 29 48<br>
63 66 04 68 89 53 67 30 73 16 69 87 40 31<br>
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
</p>

Source: [Project Euler](https://projecteuler.net/problem=18)

---

```haskell
pathSum :: [[Int]] -> Int
pathSum [[x]] = x
pathSum (xs:ys:tail) = pathSum ((mergeRows xs ys):tail)
    where
        mergeRows _ [] = []
        mergeRows (x1:x2:xs) (y:ys) = (y + max x1 x2):(mergeRows (x2:xs) ys)
```
From: Andreas | Language: Haskell

---

```python
def max_path_sum(pyramid):
    path_sum = pyramid[0][0]
    a = 0
    for i in pyramid[1:]:
        if i[a] > i[a + 1]:
            path_sum += i[a]
        else:
            path_sum += i[a + 1]
            a += 1
    print(path_sum)
```
From: Ute | Language: Python

---
