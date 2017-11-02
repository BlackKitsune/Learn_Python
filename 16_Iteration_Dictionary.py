### *** Advanced topis: Iterators for Dictionaries ***

## Iterating over a dictionary
## .items() returns array of tuples (key/value)
d = {
  "Name": "Guido",
  "Age": 56,
  "BDFL": True
}
print d.items()
# => [('BDFL', True), ('Age', 56), ('Name', 'Guido')]

my_dict = {
  "Name": "Geralt of Rivia",
  "Age": 59,
  "Magic": True
}
print my_dict.items()

## .keys() returns the list of keys
## .values() returns the list of values
print my_dict.keys()
print my_dict.values()

## "in" operator for iterating over dictionaries
for number in range(5):
  print number,

d = { 
  "name": "Eric",
  "age": 26
}

for key in d:
  print key, d[key],

for letter in "Eric":
  print letter,  # coma allows to print on the same line!

# Print  key and values with a loop
for key in my_dict:
  print key, " ", my_dict[key]
  
## Building lists: List comprehension
my_list = range(51)  # List from 0 to 50 both included

# List comprehension examples (for/in and if)
evens_to_50 = [i for i in range(51) if i % 2 == 0]
print evens_to_50

# List comprehension syntax
new_list = [x for x in range(1, 6)]
# => [1, 2, 3, 4, 5]

doubles = [x * 2 for x in range(1, 6)]
# => [2, 4, 6, 8, 10]

doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]
# => [6]

even_squares = [x ** 2 for x in range(1,12) if x % 2 == 0 ]
print even_squares

c = ['C' for x in range(5) if x < 3]
print c

cubes_by_four = [x ** 3 for x in range(1,11) if x ** 3 % 4 == 0]
print cubes_by_four

## List slicing syntax: Take part of the list[start(inclusive):end(exclusive):stride]
l = [i ** 2 for i in range(1, 11)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print l[2:9:2]

## Omitting indices (if you don't pick python uses defaults = [0:end_list:1])
to_five = ['A', 'B', 'C', 'D', 'E']

print to_five[3:]
# prints ['D', 'E'] 

print to_five[:2]
# prints ['A', 'B']

print to_five[::2]
# print ['A', 'C', 'E']

my_list = range(1, 11) # List of numbers 1 - 10
# Print only odd numbers from my_list
print my_list[::2]

## Reversing  a list (a negative stride progresses through the list from right to left)
letters = ['A', 'B', 'C', 'D', 'E']
print letters[::-1]

my_list = range(1, 11)
backwards = my_list[::-1]
print backwards

## Stride Length
to_one_hundred = range(101)
backwards_by_tens = to_one_hundred[::10]
print backwards_by_tens

to_21 = range(1, 22)
odds = to_21[::2]
middle_third = to_21[7:14]

## Anonymous fuctions: Functional programming
lambda x: x % 3 == 0
# The same as
def by_three(x):
  return x % 3 == 0

my_list = range(16)
print filter(lambda x: x % 3 == 0, my_list)

# Lambda Syntax
my_list = range(16)
filter(lambda x: x % 3 == 0, my_list)

languages = ["HTML", "JavaScript", "Python", "Ruby"]
# Return only "Python"
print filter(lambda x: x == "Python", languages)

cubes = [x ** 3 for x in range(1, 11)]
filter(lambda x: x % 3 == 0, cubes)

squares = [x ** 2 for x in range(1,11)]
print filter(lambda x: x in range(30,71), squares)

## Recap
# .items() .keys() .values()
movies = {
  "Monty Python and the Holy Grail": "Great",
  "Monty Python's Life of Brian": "Good",
  "Monty Python's Meaning of Life": "Okay"
}
print movies.items()

# List comprehension
threes_and_fives = [x for x in range(1, 16) if x % 3 == 0 or x % 5 == 0]
print threes_and_fives

# List Slicing
garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
message = garbled[::-2]
print message

# Lambda expressions
my_list = range(16)
filter(lambda x: x % 3 == 0, my_list)

garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message = filter(lambda x: x != "X", garbled)
print message

