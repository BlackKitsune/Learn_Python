### *** Introduction to Bitwise Operators ***

## Bitwise operations: operations that manipulate bits

## Basic Bitwise operators
print 5 >> 4  # Right Shift
print 5 << 1  # Left Shift
print 8 & 5   # Bitwise AND
print 9 | 4   # Bitwise OR
print 12 ^ 42 # Bitwise XOR
print ~88     # Bitwise NOT
# => 0, 10, 0, 13, 38, -89

## Base 2 Number System (0,1)
## 0 = 0, 1 = 1, 2 = 10, 3 = 11, 4 = 100, 5 = 101,...
## In python binary numbers start with 0b
print 0b1,    #1
print 0b10,   #2
print 0b11,   #3
print 0b100,  #4
print 0b101,  #5
print 0b110,  #6
print 0b111   #7
print "******"
print 0b1 + 0b11
print 0b11 * 0b11

one = 0b1
two = 0b10
three = 0b11
four = 0b100
five = 0b101
six = 0b110
seven = 0b111
eight = 0b1000
nine = 0b1001
ten = 0b1010
eleven = 0b1011
twelve = 0b1100

2 ** 0 = 1
2 ** 1 = 2
2 ** 2 = 4
2 ** 3 = 8
2 ** 4 = 16
2 ** 5 = 32
2 ** 6 = 64
2 ** 7 = 128
2 ** 8 = 256
2 ** 9 = 512
2 ** 10 = 1024

## bin() function takes an int and transform to binary
## oct() for base 8 and hex() for base 6
print bin(1)
print bin(2)
print bin(3)
print bin(4)
print bin(5)

## int(bin_number, base)
print int("1",2)
print int("10",2)
print int("111",2)
print int("0b100",2)
print int(bin(5),2)
# Print out the decimal equivalent of the binary 11001001.
print int("11001001",2)

## Slide to the left/right (<< / >>)
## Similar to rounding down after dividing and multiplying by 2
## Shifting all the 1/0 left/right specifiying the number of slots

# Left Bit Shift (<<)  
0b000001 << 2 == 0b000100 (1 << 2 = 4)
0b000101 << 3 == 0b101000 (5 << 3 = 40)       

# Right Bit Shift (>>)
0b0010100 >> 3 == 0b000010 (20 >> 3 = 2)
0b0000010 >> 2 == 0b000000 (2 >> 2 = 0)

shift_right = 0b1100
shift_left = 0b1

shift_right = shift_right >> 2
shift_left = shift_left << 2

print bin(shift_right)
print bin(shift_left)

## AND bit operator (&)
## Compare bit numbers and returns a 1 when both elements are 1
0 & 0 = 0
0 & 1 = 0
1 & 0 = 0
1 & 1 = 1

print bin(0b1110 & 0b101)

## OR bit operator (|)
## compare bit numbers and returs 1 when either element is 1
0 | 0 = 0
0 | 1 = 1 
1 | 0 = 1
1 | 1 = 1

print bin(0b1110 | 0b101)

## XOR operator (^ exclusive operator)
## compare bit numbers and returns when one element is 1
0 ^ 0 = 0
0 ^ 1 = 1
1 ^ 0 = 1
1 ^ 1 = 0

print bin(0b1110 ^ 0b101)

## NOT operator (~) flips the bits
## Adds one to the number and makes it negative
print ~1
print ~2
print ~3
print ~42
print ~123

## Bit mask (aids for bit operators)
# Example: Is the 3 bit on?
# variable containing number 12
num  = 0b1100
# mask with the 3 bit on
mask = 0b0100
# Bitwise AND to see if the 3 is on
desired = num & mask
# If the number is > 0 the is on
if desired > 0:
  print "Bit was on"

def check_bit4(input):
  mask = 0b1000
  check = input & mask
  if check > 0:
    return "on"
  else:
    return "off"
  
print check_bit4(0b1) # ==> "off"
print check_bit4(0b11011) # ==> "on"
print check_bit4(0b1010) # ==> "on"

# Use a mask to turn on the bit OR
a = 0b110 # 6
mask = 0b1 # 1
desired =  a | mask # 0b111, or 7

a = 0b10111011
mask = 0b100
desired = a | mask
print bin(desired)

# Flip it out XOR
a = 0b110 # 6
mask = 0b111 # 7
desired =  a ^ mask # 0b1

a = 0b11101110
mask = 0b11111111 
desired =  a ^ mask
print bin(desired)

## Slip and slide (slide mask into place with >> / <<)
a = 0b101 
# Tenth bit mask
mask = (0b1 << 9)  # One less than ten 
desired = a ^ mask

def flip_bit(number, n):
  bit_to_flip = 0b1 << (n -1)
  result = number ^ bit_to_flip
  return bin(result)

