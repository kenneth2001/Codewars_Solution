# Printer Errors

## Description

`printer_error` which given a string will return the error rate of the printer as a string representing a rational whose numerator is the number of errors and the denominator the length of the control string. Don't reduce this fraction to a simpler expression.

The string has a length greater or equal to one and contains only letters from `a` to `z`.

#### Examples:
    s="aaabbbbhaijjjm"
    printer_error(s) => "0/14"

    s="aaaxbbbbyyhwawiwjjjwwm"
    printer_error(s) => "8/22"
## Test Cases

	"aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz" -> "3/56"
	"kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz" -> "6/60"
	"kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyzuuuuu" -> "11/65"

## Source
https://www.codewars.com/kata/56541980fa08ab47a0000040