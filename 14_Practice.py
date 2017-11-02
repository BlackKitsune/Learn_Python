### *** Practice ***

## Determine if a number is even or not
def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False
           
print is_even(900)

## Dertermine if a number is integer or not
def is_int(x):
  if x - round(x) == 0.0:
    print x
    return True
  else:
    print x
    return False
    
print is_int(7.0)   # True    
print is_int(7.5)   # False    
print is_int(-1)    # True

## Sum the digits of a number
def digit_sum(x):
    total = 0
    while x > 0:
        total += x % 10
        x = x // 10
        print x
    return total
print digit_sum(7850)

## Function to calculate factorial of number
def factorial(x):
    total = 1
    while x>0:
        total *= x
        x-=1
    return total

print factoril(7)

## Determine if a number is prime or not
def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
              print x
              return False
        print x
        return True

print is_prime(20)
print is_prime(17)

## Reverse a word with a function
def reverse(text):
  # Empty string variable for reversed word
    word = ""
  # length of the original text for indexing
    l = len(text) - 1
  # Add the letters in reverse order
    while l >= 0:
        word = word + text[l]
        l -= 1
    return word
  
print reverse("world")

## Eliminate vowels from a word
def anti_vowel(text):
    # Define variable to store the new text
    text_no_vowels=""
    
    # for all letters in the word
    for c in text:
        # for letters in char of vocals
        for i in "ieaouIEAOU":
            # If the letter is a vowel
            if c == i:
                # remove the vowel
                c = ""
            # If it is not a vowel
            else:
                # Then do not remove
                c = c
        # Update the text_no_vowel variable
        text_no_vowels = text_no_vowels + c
    return text_no_vowels
  
print anti_vowel("Hello")

## Scrabble: Take a word and sum the value of the letters
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}

# My solution
def scramble_score(word):
  word = word.lower()
  sum = 0
  for i in word:
    sum = sum + score[i]
  return sum

print scramble_score("Hello")

# The real solution
def scrabble_score(word):
  word = word.lower()
  total = 0
  for letter in word:
    # To be sure of working with score letters and no simbols
    for leter in score:
      # If the original letter is equal to the score letter
      if letter == leter:
        # Then sum the value to total
        total = total + score[leter]
  return total

print scrabble_score("Pelicano!")

## Censor a word in a text with "*"
def censor(text, word):
  	# Split text into words elements ['ab,cs,rd'].split() = ['ab','cs','rd']
    words = text.split()
    # Variable for the resulting text
    result = ''
    # Make a char of * elements with the lenght of word
    stars = '*' * len(word)
    # Counter to 0 for the indexing of the words list
    count = 0
    
    # Main loop: for elements in the splited text
    for i in words:
        # if the element is equal to the word selected
        if i == word:
            # Then the element in the words list wil be made of *
            words[count] = stars
        # Increase indexing
        count += 1
    # Join all elements in words with a ' ' space in the middle
    result =' '.join(words)

    return result

print censor("Hello world in the world","world")

## Return the number of times an item occurs in the list
## count([1,2,1,1,],1) should return 3
def count(sequence, item):
  sum = 0
  for i in sequence:
    if i == item:
      sum += 1

  return sum

print count([1,2,2,1],1)

## Remove odd numbers from a list
def purify(sequence):
    new_sequence = []
    for element in sequence:
        if element % 2 == 0:
            new_sequence.append(element)
    return new_sequence
  
print purify([1,2,3,4,6,7,8])

## Multiply all the elements in a list
def product(integer_list):
  product_list = 1
  
  for element in integer_list:
    product_list *= element
  
  return product_list

print product([2,3,4])

## Remove the duplicates from a list
def remove_duplicates(the_list):
  new_list = []
  index = 0
  
  for element in the_list:
    if element not in new_list:
      new_list.append(element)
  index += 1
  
  return new_list

print remove_duplicates([1,2,1,3,3,7,1,8,3,4])

## Calculate the median of a list
## median = sort increasing values and locate the middle value
## In case of even number elements: average two middle elements

def median(the_list):
  the_list = sorted(the_list)
  len_list = len(the_list)
  median_list = 0.0
  
  if len_list % 2 == 0:
    # @degbug print len_list
    index1 = len_list/2
    index2 = index1 - 1
    # @debug print index1, index2
    median_list = (the_list[index1] + the_list[index2]) / 2.0
    
  else:
    # @debug print len_list
    index = len_list/2
    # @debug print index
    median_list = the_list[index]
  
  print "The median of the list is %s" %(median_list)
  
  return median_list

median([7, 3, 1, 4])
median([7, 12, 3, 1, 6])
