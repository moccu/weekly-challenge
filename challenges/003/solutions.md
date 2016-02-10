# 003: Coin sums

In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation: `1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), £2 (200p)`. It is possible to make £2 in the following way: `1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p`. How many different ways can £2 be made using any number of coins?

Source: [Project Euler](https://projecteuler.net/problem=31)


---

```erlang
coins(0, _) -> 1;
coins(_, []) -> 0;
coins(Val, _) when Val < 0 -> 0;
coins(Val, [H|T]) -> coins(Val-H, [H|T]) + coins(Val, T).
```
From: Andreas | Language: Erlang

---
