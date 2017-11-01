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

## Scrabble score
