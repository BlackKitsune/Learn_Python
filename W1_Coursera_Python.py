# 01 INTRODUCTION TO PYTHON ************************************

# Beautiful is better than ugly
# Explicit is better than implicit
# Simple is better than complex

# Install Python 3.x IDE (IDLE or Anaconda)
# IDLE url: https://python.org
# Anaconda url: https://www.continuum.io/downloads

# Example: Hello World

myString = 'Hello World!'
print(myString)
myString

# Python needs to install libraries https://pypi.python.org
# Terminal > pip > pip install name_package

# Test the use of IDE

import numpy as np
from scipy.cluster.vq import vq, kmeans, whiten

list1 = [88.0, 74.0, 96.0, 85.0]
list2 = [92.0, 99.0, 95.0, 94.0]
list3 = [91.0, 87.0, 99.0, 95.0]
list4 = [78.0, 99.0, 97.0, 81.0]
list5 = [88.0, 78.0, 98.0, 84.0]
list6 = [100.0, 95.0, 100.0, 92.0]

data = np.array([list1, list2, list3, list4, list5, list6])

whiten = whiten(data)

centroids,_ = kmeans(whiten, 2)

result,_ = vq(whiten, centroids)

print(result) # [0 1 1 0 0 1] or similar list

# Test the use of IDE

"""
Let's Plot!

"""

import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0,4,0.1)
plt.plot(t,t,t,t+2,t,t**2)

print(t)

# Output: print() for python 3

price = input('Input the stock price of Apple: ')
price
type(price)  # 'str'
# We need to change to int() to be able to work with price
price = int(input('Input the stock price of Apple: '))
# eval() consider the string as valid
price = eval(input('Input the stock price of Apple: '))


# To break the line in the code use '\'
# if (signal == 'red') and \
#       (car == 'moving'):
#           car = 'stop'

# ''' ''' Triple quotes to break the line for text
print(''' Hello everybody that is reading
this amazing code ''')

# ';' for several statements in the same line
x = 'Today'; y ='is'; z ='Monday'; print(x, y, z)

# Indentation: inside the loops, definition of functions...
# if i == 2:
#   print('Hello')  # Indented print inside the if

## 02 PYTHON BASIC SYNTAX ***************************************

# Variable
p = 3.14159
myString = 'is a mathematic circular constant'
print(p, myString)

# Identifier: Character letters, uppercase sensible
# Avoid names of Keywords: False, True, and, else, in, while ...

# Example: Math with variables
PI = 3.14159
r = 2
c_circ = 2 * PI * r
print('The circle circumference is', c_circ)

# Variable assignment (console)
PI = 3.14159
pi = PI
print(PI)
print(pi)

p = 3
q = 3
# p is q  # True

# Augmented assignment (console)
# +=, -=, /=, %=, <<=, >>= &=, ⁼, |=
m = 18
m %= 5 # m = m % 5
print(m)
m **= 2
print(m)

# Tuple (with (element1, element2))
# Multiple assignement = sequence unpaking
x = 1
y = 2
# x, y  # (1, 2)
x, y = y, x
# x, y  # (2, 1)


PI, r = 3.14159, 3
# PI  # 3.14159
# r   # 3
#(PI, r) = (3.14159, 3)

temp = 3.14159, 3  # Tuple packing
#PI, r = temp  # Sequence unpacking


# 03 DATA TYPES **************************************************

# int, float, complex, boolean, string, list, tuple and dictionary
type(3)  # int related to size memory

x = True  # Boolean
int(x)  # 1
y = False
int(y)  # 0

x = 3.22
type(x)  # float
y = 9.8e3
print(y)   # 9800.0
type(y)

x = 2.4 + 5.6j
type(x)  # complex
a = x.imag  # 5.6
b = x.real  # 2.4
c = x.conjugate  # 2.4 - 5.6j

# Sequence types: string, list, tuple, dictionary
# String (', ", ''')
myString = 'Hello world'
type(myString)  # str

# Dictionary: {key:value,...}
d ={'sine':'sin', 'cosine':'cos', 'PI':3.14159}
d['sine']  # 'sin'

# 04 BASIC OPERATIONS ***********************************************

# Arithmetic, Comparison and Logical

# Arithmetic: +, -, *, /, // (int division), ** (exp), % (reminder)
pi = 3.14159
r = 3
circum = 2 * pi * r
x = 1
y = 2
z = 3
result1 = x +3 / y - z % 2
result2 = (x + y ** y * 4) // 5
print(circum, result1, result2)

# Comparison: <, >, ==, <=, >=, !=
# 3 < 4  # True
# 4 < 3  # True
# 3 = 4  # False
# -3 != 4  # True

# Logical: not, and, or
x = -1
# x < 0.5  # True
# not(x<0.5)  # False
# (x<0.5) or (pi > 2.7)  # True
# (x<0.5) and (pi > 2.7)   # False
# not(x is y)   # True

# Raw string operator 'r'
# Error: f = open('c:\Python\test.py', 'w')
f = open(r'c:\Python\test.py', 'w')

# Bitewise operators <<, >>

## 05 FUNCTIONS, MODULES AND PACKAGES ****************************

# Prebuild functions: abs(), int(), round()...
# help(abs) to ask for help in the console
round(3.4)  # 3 round the number 3.4

# Import functions from package (libraries and modules)
# import first_level_pack.second_level_pack.py
floor(5.4)  # Error: name 'floor' not defined

from math import *  # from math library import everything
floor(5.4)  # 5

## REFERENCES *************************************************

# Python IDLE: https://www.python.org/
# Anaconda: https://www.continumm.io/downloads
# Pycharm or Jupyter notebook

# Magnus Lie Heland, Beginning Python (Apress)
# Wesley Chun, Core Python Applications Programming (Prentice Hall)
# SciPy Scientific Calculation: https:/www.scipy.org
# Wes McKinney, Python for Data analysis

## EXERCISE: Input name and surname and print both

your_name = input('What is your name?:')
your_familyname = input('What is your surname?:')

print('Your name is', your_name)
print('Your family name is', your_familyname)
print('Your full name is', your_name, your_familyname)


## 06 CONDITIONS ***************************************************

# Programm code structures: Sequence, selection and repetition

# IF statement (if expression: expression _true_suite)
sd1 = 3
sd2 = 4
if sd1 == sd2:  # True statement
    print('The square area is:', sd1*sd2)
else:  # False statement none of the above
    print('The rectangle area is', sd1*sd2)

k = input('input index of shape: ')
if k == '1':
    print('circle')
elif k == '2':
    print('oval')
elif k == '3':
    print('rectangle')
else:
    print('You input an invalid number')

# Example: this 2 code statements are equivalent? True
x = int(input('Input x:'))
if x <= 10:
    result = x * 0.1
elif x < 20:
    result = x * 10
print(result)

x = int(input('Input x:'))
if x <= 10:
    result = x * 0.1
elif x > 10 and x < 20:
    result = x * 10
print(result)

# Nested if statements
k = input('input index of shape: ')
if k == '1':
    print('circle')
elif k == '2':
    print('oval')
elif k == '3':
    sd1 = int(input('The first side:'))
    sd2 = int(input('The second side:'))
    if sd1 == sd2:
        print('Square area:', sd1*sd2)
    else:
        print('Rectangle area:', sd1*sd2)
else:
    print('You input an invalid number')

# Example: Guess number
from random import randint

# randit(start, end) = random num between start and end
x = randint(0,300)
print(x)
digit = int(input('Input a number betwee 0 and 300: '))
if digit == x:
    print('That is the number I was looking for!!')
elif digit > x:
    print('Too large, please try again')
else:
    print('Too small, please try again')


## 08 RANGE **********************************************

# range() range of num between start and en with 1 step
# range(start = 0, end, step = 1)

list(range(3,7,2))  # 3,5
list(range(3,7))    # 3,4,5,6
list(range(11))     # 0,1,2,3,4,5,6

## 09 LOOPS ***********************************************

# WHILE LOOP
# while expression == True: suite_to_repeat

# Assignment initialization
sumA = 0
j = 1
# while loop until j = 10
while j < 10:
    # suite_to_repeat
    sumA += j
    # Increase the loop value
    j += 1

# FOR LOOP (string, list, tuple, dictionary, files)
# for iter_var in iterable_object: suite_to_repeat

# String
s = 'python'
for letter in s:
    print(letter)

# List
for i in range(2,11,2):
    print(i,end = '')

# Example: Guess number

from random import randint

# randit(start, end) = random num between start and end
x = randint(0,300)
# @debug print(x)

# You will have 5 tries
for count in range(0,5):
    digit = int(input('Input a number betwee 0 and 300: '))
    if digit == x:
        print('That is the number I was looking for!!')
    elif digit > x:
        print('Too large, please try again')
    else:
        print('Too small, please try again')

# LIST COMPREHENSION

# Generate a list from 0 to 9 included with a loop
a = [i for i in range(10)]

# Generate a list with a condition with a loop
b = [i+1 for i in range(10) if i%2 == 0]

# Generator (with parenthesis in the expresion)
c = (i+1 for i in range(10) if i%2 == 0)


## 10 BREAK, CONTINUE AND ELSE LOOPS ***************************

# BREAK (stope the loop or code)
sumA = 0
i = 1
# This could be a if you don't break it
while True:
    sumA += 1
    i += 1
    # Add break statement to end the loop
    if sumA > 10:
        break

print('i={}, sum={}'.format(i,sumA))

from math import sqrt
j = 2
while j <= 100:
    i = 2
    k = sqrt(j)
    while i <= k:
        if j%i== 0: break
        i += 1
    if i > k:
        print(j,end = '')
    j += 1

flag = 1
for i in range(2,101):
    k = int(sqrt(i))
    for j in range(2,k+1):
        if i % j == 0:
            # To avoid exceptions
            break
    if flag:
        print(i,end='')

# Example: What is the result of...? 1 2

i = 1
while(i % 3):
    print(i, end='')
    if(i >= 10):
        break
    i += 1

# CONTINUE makes the code to continue

# With break
sumA = 0
i =1
while i <= 5:
    sumA += i
    if i == 3:
        break
    print('i = {}, sum= {}'.format(i,sumA))
    i += 1

# With continue
sumA = 0
i =1
while i <= 5:
    sumA += i
    if i == 3:
        continue  # skip the statemen after the continue
    print('i = {}, sum= {}'.format(i,sumA))
    i += 1

# WHILE ELSE LOOP (else substitute of break)

# Example: Guess number
from random import randint

# randit(start, end) = random num between start and end
x = randint(0,300)
go = 'y'
#  @debug print(x)

while (go == 'y'):
    digit = int(input('Input a number betwee 0 and 300: '))
    if digit == x:
        print('That is the number I was looking for!!')
    elif digit > x:
        print('Too large, please try again')
    else:
        print('Too small, please try again')
    print('Input y if you want to continue.')
    go = input()
    print('Then we continue')
else:
    print('Goodbye!')

for i in range(1,10,2):
    if i % 5 == 0:
        print('Bingo')
        break
    else:
        print(i)

## 11 SELF DEFINED FUNCTIONS ***********************************

# Built in or user defined functions
# def function_name([arguments]): function_suite

def addMe2Me(x):
    'apply operation + to argument'
    return(x+x)

print(addMe2Me(7))

# Example: Function that decides if a num is prime or not
from math import sqrt

def isprime(x):
    if x == 1:
        return False

    k = int(sqrt(x))

    for j in range(2, k+1):
        if x % j == 0:
            return False
        return True

for i in range(2,101):
    if isprime(i):
        print(i, end = ' ')

# Exercise: Is this deciding prime number correctly? Incorrect

from math import sqrt

def isprime(x):
    if x == 1:
        return False

    k = int(sqrt(x))

    for j in range(2, k+1):
        if x % j == 0:
            return False
        else:
            return True

for i in range(2,101):
    if isprime(i):
        print(i, end = ' ')

# Arguments by default (key arguments)
def f(x = True):
    'Whether x is a correct word or not'
    if x:
        print('x is a correct word')
    print('OK')

f()
f(False)

def f(x, y = True):
    'x and y are both words or not'
    if y:
        print(x, 'and y both correct')
    print(x, 'is ok')

f(68)
f(68,False)

# Transfer function (addMe2Me() inside anothe function self())
def addMe2Me(x):
    return(x+x)

def self(f,y):
    print(f(y))

self(addMe2Me, 2.2)

# Lambda functions. one line func(the same as addMe2Me())
# lambda elements: Do something with elements
r = lambda x: x+x
r(5)

## 12 RECURSION ************************************************

# Fibonacci series as example of recursion
# Return the nth fibonacci number

# With a loop
def fib(n):
    a, b = 0, 1
    count = 1
    while count < n:
        a, b = b, a+b
        count = count + 2
    print(a)

fib(6)

# With recursion
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

fib(6)

# The Hanoi tower algorithm resolution
# a, b and c ar the towers and n the number of disks in the a tower
def hanoi(a,b,c,n):
    if n==1:
        print(a,'->',c)
    else:
        hanoi(a,c,b,n-1)
        print(a,'->',c)
        hanoi(b,a,c,n-1)

hanoi('a','b','c',4)

def foo(num,base):
    if(num >= base):
        foo(num // base , base)
    print(num%base, end = ' ')

numA = int(input())
numB = int(input())
foo(numA, numB)

## 13 SCOPE OF VARIABLE ****************************************

# Global and local variables

global_str = 'Hello'
def foo():
    local_str = 'world'
    return global_str, local_str

a = 3  # global
def f():
    a = 5  # local
    print(a**2)

# Define the variables inside the function as global
def f(x):
    global a
    print(a)
    a = 5
    print(a+x)

a = 3
f(8)
print(a)

## PROGRAM QUIZZES *********************************************

# 1. Program for input scores and output grades of scores
# Score	Grade 90~100 A, 70~89 B, 60~69 C, 0~59 D, others Invalid score

def grade(score):
    if score >= 90 and score <= 100:
        print('A')
    elif score >= 70 and score <= 89:
        print('B')
    elif score >= 60 and score <= 69:
        print('C')
    elif score >= 0 and score < 59:
        print('D')
    else:
        print('Invalid Score')

grade(100)
grade(95)
grade(87)
grade(75)
grade(62)
grade(55)
grade(123)
grade(0)

# 2. Verify one of the Goldbach conjecture:
# Positive int num (>= 4) within 2000 can be decomposed into the sum
# of two prime numbers.
# Every even numbers expression forming is such as 4 = 2+2
# print 6 expreseions per line

# 3. Program to let user input a number of apples, the unit price and
# calculate the total

while True:
    try:
        count = int(input("Enter count: "))
        price = int(input("Enter price for each one: "))
        Pay = count * price
        print("The price is: ", Pay)
        break
    except ValueError:
        print('Error, please enter numeric one. ')


## A1 STANDARD LIBRARY FUNCTIONS **************************************

# import math: mathematic operations
import math
dir(math)  # functions inside the math module
math.pi
math.e
help(math.ceil)
math.ceil(3.6)
math.floor(3.6)
math.pow(2,3)
math.degrees(3.14)
math.radians(180)

# import os: interacting with the operation system
import os
os.getcwd()
path = 'c:\\text'
os.chdir(path)
os.getcwd()
os.rename(old_filename, new_filename)
os.remove(filename)

# import random: Generation of random values
import random
random.choice(['C++', 'Java', 'Python'])  # Choose one random from list
random.randint(1,100)  # Choose one random int from range
random.randrange(0,10,2)
random.random()
random.uniform(5, 10)  # floating number
random.sample(range(100))  # returns a random list
nums = [1, 2, 3, 4]
random.shuffle(nums)  # reorders randomly the list
random.choice(['Leonard', 'Sheldon', 'Penny', 'Howard', 'Raj', 'Bernadette', 'Amy'])

# import datetime
import datetime
dir(datetime)  # functions inside datetime module
from datetime import date
date.today()
from datetime import time
tm = time(23, 20, 35)
print(tm)
from datetime import datetime
dt = datetime.now()
# formats: a day of the week, b month, c day, ...
print(dt.strftime('%a, %b %c %d %Y %H:%M'))
# Time stamp epoch 1971-01-01 00:00:00 is time = 0s
dt = datetime(2017, 6, 6, 2, 29)
print(dt)
ts = dt.timestamp()  # to epoch
print(datetime.fromtimestampp(ts))

## A2 EXCEPTIONS ************************************************************

# How to treat errors: 1/0 will lead to an exception
# >>> 1/0
# Traceback (most recent call last): --> Mesagge of error (traceback)
#   File "<input>", line 1, in <module>
# ZeroDivisionError: division by zero  --> Type of exception

# We can sue __builtins__() for looking to exceptions types
dir(__builtins__)  # all built in exceptions classes

if y != 0:
    print(x/y)
else:
    print('Division by zero')

# try - except format
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))  # Can be 0 or a letter
print(num1/num2)  # Leading to exception

try:
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))  # Can be 0 or a letter
    print(num1/num2)  # Leading to exception
except ValueError:
    print('Please input a digit!')

except ZeroDivisionError as err:  # err = error cause
    print('The second number can not be zero!')
    print(err)

try:
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))  # Can be 0 or a letter
    print(num1/num2)  # Leading to exception

except (ValueError, ZeroDivisionError):  # Several exceptions
    print('Invalid input!')

# General case
try:
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))  # Can be 0 or a letter
    print(num1/num2)  # Leading to exception

except Exception as err:  # General case
    print('Something went wrong!')
    print(err)

# try - except - else
try:
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))  # Can be 0 or a letter
    print(num1/num2)  # Leading to exception

except (ValueError, ZeroDivisionError):  # Several exceptions
    print('Invalid input!')
else:
    print('Everything is OK')

# Retry option with while/if loop  -- break statement
while True:
    try:
        num1 = int(input('Enter first number: '))
        num2 = int(input('Enter second number: '))  # Can be 0 or a letter
        print(num1/num2)  # Leading to exception
        break  # Add the break statement
    except (ValueError, ZeroDivisionError):  # Several exceptions
        print('Invalid input!')

# break statement is not necesarly inside the try block
while True:
    try:
        num1 = int(input('Enter first number: '))
        num2 = int(input('Enter second number: '))  # Can be 0 or a letter
        print(num1/num2)  # Leading to exception
    except (ValueError, ZeroDivisionError):  # Several exceptions
        print('Invalid input!')
    else:
        break  # Add the break statement

a_list = [1,2,3,4,5]
i = 0
while True:
    try:
        print(a_list[i])
    except IndexError:
        print('Index Error')
        break
    else:
        i += 1

# Complete code with finally
def finallyTest():
    while True:
        try:
            num1 = int(input('Enter first number: '))
            num2 = int(input('Enter second number: '))  # Can be 0 or a letter
            print(num1/num2)  # Leading to exception
            return 1
        except Exception as err:  # Several exceptions
            print('Invalid input!')
            print(err)
            return 0
        finally:
            print('It is a finally clause.')
result = finallyTest()
print(result)

# Context manager (with statement)
try:
    f = open('data.txt')
    for line in f:
        print(line, end= ' ')
except IOError:
    print('Cannot open the file')
finally:
    f.close()

with open('data.txt') as f:  # The same as before
    for line in f:
        print(line, end='')

# Exercise: Program to let user input a number of apples, the unit price and
# calculate the total. With exception error for non numerical inputs.

while True:
    try:
        count = int(input("Enter count: "))
        price = int(input("Enter price for each one: "))
        Pay = count * price
        print("The price is: ", Pay)
        break
    except ValueError:
        print('Error, please enter numeric one. ')

## TEST: CHARACTERISTICS OF A RECURSIVE ALGORITHM ***************************

# Figure out the result of the following program (do not use a computer)
def proc(n):
    if n < 0:
        print('-', end = '')
        n = -n
    if n  // 10:
        proc(n  //  10 )
    print(n % 10,  end = '')

proc(-345 )

# output -345 (first if prints - and second if 345)

## QUIZZ *********************************************************************

k = 50
while k > 1:
    print(k)
    k = k // 2

apples = 100
while apples >= 1:
    if apples < 9:
        print("rest apples are less than 9")
        break
    apples -= 9

def location(city, province):
    print('%s belongs to %s province' % (city, province))

location(province = 'Jiangsu', city = 'Nanjing')

location('Jiangsu', 'Nanjing')

location('Nanjing', 'Jiangsu')

location(city = 'Nanjing', province = 'Jiangsu')

def test(f, a, b):
    print(f(a, b))

test((lambda x,y: x ** 3 + y), 2, 3)

## w1 PROGRAMMING ASSIGNMENT ************************************************

# Find out the 6th Monisen number
# A number M is a Monisen number if M = 2**P-1 and both M and P
# are prime numbers.
# Ex: if P = 5, M = 2**P-1=31, 5 and 31 are both prime numbers
# so 31 is a Monisen number

from math import sqrt

def prime(num):
    # Be sure to have an integer num
    num = int(num)

    # Less than 2 no prime numbers
    if num <=1:
        return False

    # If the element is % 2,...
    N = int(sqrt(num))
    for i in range(2, N+1):
        if num % i == 0:
            return False
            break

    # if you have not returned False
    # Then is prime number
    return True

def monisen(n):
    if n >= 1:
        i = 0
        num = 2

        while True:
            m = 2 ** num - 1

            if prime(num) and prime(m):
                i += 1
            num += 1

            if i == n:
                break

        return m
    else:
        return 0

print(monisen(6))  # 131071




