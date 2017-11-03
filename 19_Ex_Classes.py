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
    print "This is a %s %s with %s MPG." % (self.color, self.model, str(self.mpg))
  
  # Modify condition member variable
  def drive_car(self):
    self.condition = "used"

  
# Create an instance of a class
my_car = Car("DeLorean", "silver", 88)

# Print the member value condition
print my_car.condition

# Print the variables of the car
print my_car.model
print my_car.color
print my_car.mpg

# Print the same information with the display method
my_car.display_car()

# Check befor and after car condition 
print my_car.condition
my_car.drive_car()
print my_car.condition

# Inheritance
class ElectricCar(Car):
  def __init__(self, model, color, mpg, battery_type):
    self.model = model
    self.color = color
    self.mpg   = mpg
    self.battery_type = battery_type

my_car = ElectricCar("DeLorean", "silver", 88, "molten salt")

print my_car.condition
my_car.drive_car()
print my_car.condition

## Recap
class Point3D(object):
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z
  
  def __repr__(self):
    return "(%d, %d, %d)" % (self.x, self.y, self.z)
  
my_point = Point3D(1,2,3)
print my_point
