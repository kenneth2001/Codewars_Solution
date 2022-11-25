# Is this a triangle?

## Description

Implement a function that accepts 3 integer values a, b, c. The function should return true if a triangle can be built with the sides of given length and false in any other case.

(In this case, all triangles must have surface greater than 0 to be accepted).

## Test Cases

	1, 2, 2 -> True
	7, 2, 2 -> False
	1, 2, 3 -> False
	1, 3, 2 -> False
	3, 1, 2 -> False
	5, 1, 2 -> False
	1, 2, 5 -> False
	2, 5, 1 -> False
	4, 2, 3 -> True
	5, 1, 5 -> True
	2, 2, 2 -> True
	-1, 2, 3 -> False
	1, -2, 3 -> False
	1, 2, -3 -> False
	0, 2, 3 -> False

## Source
https://www.codewars.com/kata/56606694ec01347ce800001b/train/python