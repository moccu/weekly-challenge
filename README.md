# Weekly Programming Challenge

## 001: Add up multiples

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1001.

Source: [Project Euler](https://projecteuler.net/problem=1)

Solutions: [Challenge001](challenges/001/solutions.md)

## 002: Run-length encoding of a list

Implement the so-called run-length encoding data compression method. Consecutive duplicates of elements are encoded as lists (N E) where N is the number of duplicates of the element E.

```javascript
encode([a, a, a, b, b, c, a, a]) == [[3, a], [2, b], [1, c], [2, a]]
```

Source: [99 Prolog Problems](http://www.ic.unicamp.br/~meidanis/courses/mc336/2009s2/prolog/problemas/p10.pl)

Solutions: [Challenge002](challenges/002/solutions.md)

## 003: Coin sums

In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation: `1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), £2 (200p)`. It is possible to make £2 in the following way: `1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p`. How many different ways can £2 be made using any number of coins?

Source: [Project Euler](https://projecteuler.net/problem=31)

Solutions: [Challenge003](challenges/003/solutions.md)

## 004: Round Robin Tournament

Solutions: [Challenge004](challenges/004/solutions.md)

## 005: Bubble sort

Bubble sort, sometimes referred to as sinking sort, is a simple sorting algorithm that repeatedly steps through the list to be sorted, compares each pair of adjacent items and swaps them if they are in the wrong order. The pass through the list is repeated until no swaps are needed, which indicates that the list is sorted.

Source: [Wikipedia](https://en.wikipedia.org/wiki/Bubble_sort)

Solutions: [Challenge005](challenges/005/solutions.md)

## 006: Maximum path sum

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

Solutions: [Challenge006](challenges/006/solutions.md)
