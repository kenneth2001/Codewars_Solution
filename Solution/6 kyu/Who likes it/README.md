# Who likes it?

## Description 

You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

Implement a function likes :: [String] -> String, which must take in input array, containing the names of people who like an item. It must return the display text as shown in the examples:

    likes [] // must be "no one likes this"
    
    likes ["Peter"] // must be "Peter likes this"
    
    likes ["Jacob", "Alex"] // must be "Jacob and Alex like this"
    
    likes ["Max", "John", "Mark"] // must be "Max, John and Mark like this"
    
    likes ["Alex", "Jacob", "Mark", "Max"] // must be "Alex, Jacob and 2 others like this"

## Test Cases

    [] -> 'no one likes this'
    ['Peter'] -> 'Peter likes this'
    ['Jacob', 'Alex'] -> 'Jacob and Alex like this'
    ['Max', 'John', 'Mark'] -> 'Max, John and Mark like this'
    ['Alex', 'Jacob', 'Mark', 'Max'] -> 'Alex, Jacob and 2 others like this'
    
## Source
https://www.codewars.com/kata/5266876b8f4bf2da9b000362/train/python
