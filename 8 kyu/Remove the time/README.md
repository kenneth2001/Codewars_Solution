# Remove the time

## Description 

You're re-designing a blog and the blog's posts have the following format for showing the date and time a post was made:

Weekday Month Day, time e.g., Friday May 2, 7pm

You're running out of screen real estate, and on some pages you want to display a shorter format, Weekday Month Day that omits the time.

Write a function, shortenToDate, that takes the Website date/time in its original string format, and returns the shortened format.

Assume shortenToDate's input will always be a string, e.g. "Friday May 2, 7pm". Assume shortenToDate's output will be the shortened string, e.g., "Friday May 2".

## Test Cases

    "Monday February 2, 8pm" -> "Monday February 2"
    "Tuesday May 29, 8pm" -> "Tuesday May 29"
    "Wed September 1, 3am" -> "Wed September 1"
    "Friday May 2, 9am" -> "Friday May 2"
    "Tuesday January 29, 10pm" -> "Tuesday January 29"

## Source
https://www.codewars.com/kata/56b0ff16d4aa33e5bb00008e/train/python
