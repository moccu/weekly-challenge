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

```python
def count_combinations_fast(amount, values, current=0):
    if amount == 0:
        return 1

    if amount < 0 or len(values) == current:
        return 0

    with_current_value = count_combinations_fast(amount - values[current], values, current)
    without_current_value = count_combinations_fast(amount, values, current + 1)
    return with_current_value + without_current_value


def count_combinations(amount, values, current=0, selected=None):
    # Initialize list of selected values if uninitialized.
    if selected is None:
        selected = []

    # We matched the exact target value, means found one combination.
    if amount == 0:
        print('Valid combination', selected)
        return 1

    # Negative amount, means last value was to large, we remove the value from
    # the list of selected values to continue properly.
    if amount < 0 or len(values) == current:
        if selected:
            print('Invalid combination', selected)
            selected.pop()
        return 0

    # Continue calculation with amount reduced by current value, also append the
    # current value to our list of selected values.
    with_current_value = count_combinations(
        amount - values[current], values, current, selected + [values[current]])
    # Also try to match the target amount by skipping the current value.
    without_current_value = count_combinations(amount, values, current + 1, selected)

    # Return sum of both combinations with current value and without.
    return with_current_value + without_current_value


if __name__ == '__main__':
    print('Total combinations #1', count_combinations_fast(200, [1, 2, 5, 10, 20, 50, 100, 200]))
    print('Total combinations #2', count_combinations(20, [5, 10, 20]))
```
From: Stephan | Language: Python

---

```c
#include <stdint.h>
#include <stdio.h>


int32_t cnt(int32_t a, uint8_t *v, uint8_t t, uint8_t i) {
	if (a == 0) return 1;
	if (a < 0 || i >= t) return 0;
	return cnt(a - v[i], v, t, i) + cnt(a, v, t, i + 1);
}

int32_t cnt_start(int32_t a, uint8_t *v) {
	return cnt(a, v, sizeof(v) / sizeof(v[0]), 0);
}

int main(void) {
	printf("%d\n", cnt_start(200, (uint8_t[]) {1, 2, 5, 10, 20, 50, 100, 200}));
	return 0;
}
```
From: Stephan | Language: C

---
