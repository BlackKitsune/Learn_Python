### *** Input and Output: I/O ***

## Output to a text file
# Generates a list of squares of the numbers 1 - 10
my_list = [i ** 2 for i in range(1, 11)]

# Open the ouput.txt file and write on it
# Store the result of this operation in a file object f
f = open("output.txt", "w")

# Iterate trough the list
for item in my_list:
  # Write inside output.txt (now f object)
  # one item in each line (\n)
  # And transforming the item to string
  f.write(str(item) + "\n")

# Close f object, if not is not written
f.close()


# Example:
my_list = [i ** 2 for i in range(1, 11)]

# r+ will allow to read and write 
my_file = open("output.txt", "r+")

for item in my_list:
  my_file.write(str(item) + "\n")
  
my_file.close()

## Reading from a file
# r statement from read
my_file = open("output.txt", "r")

print my_file.read()

my_file.close()

## Read line by line (.readline())
my_file = open("text.txt", "r")

# Read 3 lines from text.txt
print my_file.readline()
print my_file.readline()
print my_file.readline()

my_file.close()

## PSA: Buffering Data
# data is stored in the buffer before
# when the file is closed is written

# Use a file handler to open a file for writing
write_file = open("text.txt", "w")
write_file.close()

# Open the file for reading
read_file = open("text.txt", "r")
read_file.close()

# Write to the file
write_file.write("Not closing files is VERY BAD.")

# Try to read from the file
print read_file.read()

## Automaticaly close files ("with" and "as" keywords)
# File objects contain special pair of built in methods
# __enter__() and __exit__()
# A file object __exit__() method automatically closes the file
# This is done with "with" and "as"

# with open("file", "mode") as variable:
  # Read or write to the file
  
with open("text.txt", "w") as textfile:
  textfile.write("Success!")

with open("text.txt", "w") as my_file:
  my_file.write("Geralt the Rivia is a Witcher")
  
## Test if the file is closed
f = open("bg.txt")
f.closed
# False
f.close()
f.closed
# True

with open("text.txt", "w") as my_file:
  my_file.write("Geralt the Rivia is a Witcher")

if my_file.closed == False:
  my_file.close()

print my_file.closed



