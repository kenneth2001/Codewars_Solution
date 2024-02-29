# Strip Comments

## Description 

Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

Example:

    apples, pears # and bananas
    grapes
    bananas !apples

The output expected would be:

    apples, pears
    grapes
    bananas

The code would be called like so:

    result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
    # result should == "apples, pears\ngrapes\nbananas"

## Test Cases

    "apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"] -> "apples, pears\ngrapes\nbananas"
    "a #b\nc\nd $e f g", ["#", "$"] -> "a\nc\nd"

## Source
https://www.codewars.com/kata/51c8e37cee245da6b40000bd/train/python