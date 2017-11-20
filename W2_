## W2 DATA ADQUISITION AND PRESENTATION **********************************************

## Read data from files (open file, do something, close the files)
# file_obj = open(filenam, mode='r', buffering= -1, ...)
# mode = 'r', 'w', 'a' to read, write and append (with a b 'rb' for binary files)
# mode = 'r+', 'w+', 'a+' to r+w, w+r and a+r
# buffering = -1 is use the default size of the machine
# help(open) to see details

f1 = open('d://infile.txt')
f2 = open(r'd://outfile.txt', 'w')
f2 = open('record.dat', 'wb',0)

# f.read(), f.write(), f.readline(), f.readlines(), f.writelines()
# f.close()
# f.seek()

## Writting data to file
f = open('firstpro.txt', 'w')
f.write('Hello, world!')
f.close()

# It is better to write into file with a 'with' statement to handle exceptions
with open('firstpro.txt', 'w') as f:
  f.write('Hello, world!')
  
## Reading data from file
# file_obj.read(size)
# file_obj.read()

with open('firstpro.txt', 'r') as f:
    p1 = f.read(5)  # Hello
    p2 = f.read()  # , world (rest of the file)
    print(p1)
    print(p2)
    print(p1, p2)
    
with open('firstpro.txt', 'r') as f:
    p1 = f.read()
    p2 = f.read()
    print(p2)  # ouput empthy, the pointer has reached the tail of the file

# The file pointer may be viewed through f.tell(). Upon completion of running f.read()
# the file pointer has reached the end of file. So, there is no ouput when running
# f.read() again

## Other functions line by line
# file_obj.readline()
# file_obj.readlines()
# file_obj.writelines()

# companies.txt = ['Google \n', 'Microsoft \n', 'Facebook \n']
with open('companies.txt', 'r') as f:
  cNames = f.readlines()
  print(cNames)
  
with open('companies.txt', 'r') as f1:
    cNames = f1.readlines()
    # Add the number of the lines str(num) = comvert to string
    for i in range(0, len(cNames)):
        cNames[i] = str(i+1) + ' ' + cNames[i]
# Store this new info into a new file
with open('scompanies.txt', 'w') as f2:
    f2.writelines(cNames)
    
# Add a sentence to the tile of the file
s = 'Tencent Technology'
with open('companies.txt', 'a+') as f:
  f.writelines('\n')
  f.writelines(s)
  # bring the file pointer to a specific line with f.seek()
  # f.seek(offset, whence=0) = (start, +lines from start)
  f.seek(0,0)  # Move the file pointer to the head of the file
  # f.seek(50,1)  # Move the file pointer 50 lines back
  cNames = f.readlines()
  print(cNames)

## Standard files
# input(), print() functions with ask/display in the screen
# stdin/stdout, and sterr are the same in sys library
import sys
sys.stout.write('Hell')

