# 005: Bubble sort

Bubble sort, sometimes referred to as sinking sort, is a simple sorting algorithm that repeatedly steps through the list to be sorted, compares each pair of adjacent items and swaps them if they are in the wrong order. The pass through the list is repeated until no swaps are needed, which indicates that the list is sorted.

Source: [Wikipedia](https://en.wikipedia.org/wiki/Bubble_sort)

---

```scss
$random-list: 0;
//generate random list
@for $i from 1 through 24 {
	$random-list: append($random-list, random(100));
}

@function bubble-sort($list) {
	$result: $list;
	$length: length($result);

	//length of list -1
	@for $i from 1 through $length - 1 {

		//move through list
		@for $n from 1 through $length - $i {

			@if nth($result, $n) > nth($result, $n + 1) {
				//swap
				$max: nth($result, $n);
				$min: nth($result, $n + 1);
				$result: set-nth($result, $n + 1, $max);
				$result: set-nth($result, $n, $min);
			}
		}
	}
	@return $result;
}

body {

	&:before {
		content: '#{$random-list}';
	}

	&:after {
		 content: '#{bubble-sort($random-list)}'
	}
}
```
From: Jannik | Language: scss

---
