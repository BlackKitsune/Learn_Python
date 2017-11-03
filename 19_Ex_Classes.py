### *** Class interactive lesson ***

## Defining a class is like defining a function, with class keyword
# The (object) allows the class to inherit the object class
# Meaning that the class has all the properties of an object (simplest class)

# Create a class called "Car"
class Car(object):
  # Member variables (with initial values)
  condition = "new"
  def __init__(self, model, color, mpg):
    self.model = model
    self.color = color
    self.mpg = mpg
    
  # Define a class method
  def display_car(self):
    print "This is a %s %s with %s MPG" %(self.color, self.model, str(self.mpg))
  
  

# Create an instance of a class
my_car = Car("DeLorean", "silver", 88)

# Print the member value condition
print my_car.condition

# Print the variables of the car
print my_car.model
print my_car.color
print my_car.mpg
