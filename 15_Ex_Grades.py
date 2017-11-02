### *** Compute statistics from grades ***

## Create a list with the grades
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]
print "Grades:", grades

## Print the grades one by one
def print_grades(grades_input):
  for element in grades_input:
    print element

print_grades(grades)

## Compute some statistics with the grades
print "Let's compute some stats with the grades!"

# Sum of the scores
def grades_sum(scores):
  total = 0
  for element in scores:
    total += element
  
  return total

print "Sum of all the grades: %s" %(grades_sum(grades))

## Average of the scores
def grades_average(grades_input):
  sum = grades_sum(grades_input)
  average = sum / float(len(grades_input))
  
  return average

print "Average of the grades: %s" %(grades_average(grades))

## Compute the variance
## small variance close to the average means the majority did fairly well
## large variance that there are a lot of variability in the grades (not good)
print "Time to conquer the variance!"


def grades_variance(scores):
  average = grades_average(scores)
  variance = 0
  
  for score in scores:
    variance += (average - score) ** 2
  
  variance = variance / len(scores)
  
  return variance

print "The variance of the grades is: %s" %(grades_variance(grades))

## Compute the standard deviation
## Square root (**0.5) of the variance

variance = grades_variance(grades)

def grades_std_deviation(variance):
  return variance ** 0.5

std_deviation = grades_std_deviation(variance)

print "The standard deviation of the grades is: %s" %(std_deviation)

## Print statistics
print "The grades: " 
print_grades(grades)

print ""
print "**** The statistics for the grades ****"
print ""

sum = grades_sum(grades)
print "Sum: %s" %(sum)

average = grades_average(grades)
print "Average: %s" %(average)

variance = grades_variance(grades)
print "Variance: %s" %(variance)

std_deviation = grades_std_deviation(variance)
print "Tstandard Deviation: %s" %(std_deviation)

## The solution from course
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades_input):
  for grade in grades_input:
    print grade

def grades_sum(scores):
  total = 0
  for score in scores: 
    total += score
  return total
    
def grades_average(grades_input):
  sum_of_grades = grades_sum(grades_input)
  average = sum_of_grades / float(len(grades_input))
  return average

def grades_variance(grades):
    variance = 0
    for number in grades:
        variance += (grades_average(grades) - number) ** 2
    return variance / len(grades)

def grades_std_deviation(variance):
  return variance ** 0.5

variance = grades_variance(grades)

for grade in grades:
  print grade
print grades_sum(grades)
print grades_average(grades)
print grades_variance(grades)
print grades_std_deviation(variance)





