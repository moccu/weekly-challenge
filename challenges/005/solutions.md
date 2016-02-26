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
``` cobol
       identification division.
       program-id. BUBBLSORT.
       data division.
       working-storage section.
      * Field level 88 is magic: makes easier qual tests, if hasChanged
      * vs. if changed-flag is equal to "Y"
       01 changed          pic x.
           88 hasChanged        value 'Y'.
           88 hasNotChanged     value 'N'.

      * Stores acutal array to sort, max number is 99999 (5 digits).
      * Handles max. 32 items.
       01 items.
           02 itemLength    pic 9(2).
           02 itemPosition  pic 9(2).
           02 item          pic 9(5) occurs 32 times.

      * Later needed to store value when swapping.
       01 tempItem          pic 9(5).

      * Remember the current positionition while looping through array.
       01 currentPosition   pic 9(2).

       procedure division.
       main.
      * place the values to sort into itemArray
           move 10 to itemLength
           move 23 to item (1)
           move 74 to item (2)
           move 34 to item (3)
           move 67 to item (4)
           move 12 to item (5)
           move 18 to item (6)
           move 10 to item (7)
           move 99 to item (8)
           move 19 to item (9)
           move 13 to item (10)

           perform bubble-sort

           perform varying itemPosition from 1 by 1
               until itemPosition > itemLength
               display itemPosition ') ' item(itemPosition)
           end-perform
           stop run.

       bubble-sort.
      * Remember array length as current currentPositionition.
           move itemLength to currentPosition

      * Loop through array until we have nothing swapped
           perform with test after until hasNotChanged
      * Nothing changed until now..
               set hasNotChanged to true
               subtract 1 from currentPosition
      * Loop through remaining unsorted items.
               perform varying itemPosition from 1 by 1
                   until itemPosition > currentPosition
      * Check if current item is greater than next item.
                   if item(itemPosition) > item(itemPosition + 1)
                       move item(itemPosition) to tempItem
                       move item(itemPosition + 1) to item(itemPosition)
                       move tempItem to item(itemPosition + 1)
                       set hasChanged to true
                   end-if
               end-perform
           end-perform
           .
```
From: Stephan | Language: Cobol

---
```python
bubbles = [3, 6, 1, 5, 23, 33, 3, 3, 3, 11, 9, 46, 78, 21]
running = True

while running:
    running = False
    for i, item in enumerate(bubbles, start=1):
        if i == len(bubbles):
            break

        if item > bubbles[i]:
            bubbles[i - 1], bubbles[i] = bubbles[i], item
            running = True
```
From: Ben | Language: python

---
