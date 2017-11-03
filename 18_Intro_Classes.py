### *** Introcduction to Classes ***

## Python is object oriented language
# Object: Single data structure that contains data as well as functions
# The functions of an object are called its methods
# Classes are a way of organizing and producing objects with similar attirbutes and methonds

# Example of class definition:
class Fruit(object):
  """A class that makes various tasty fruits."""
  def __init__(self, name, color, flavor, poisonous):
    self.name = name
    self.color = color
    self.flavor = flavor
    self.poisonous = poisonous

  def description(self):
    print "I'm a %s %s and I taste %s." % (self.color, self.name, self.flavor)

  def is_edible(self):
    if not self.poisonous:
      print "Yep! I'm edible."
    else:
      print "Don't eat me! I am super poisonous."

lemon = Fruit("lemon", "yellow", "sour", False)

lemon.description()
lemon.is_edible()

## Class syntax (class name_class(object): The class with inherit from object)
# class NewClass(object):
  # Class magic here

class Animal(object):
  pass  # Doesn't do anything
  
## __init__(self, arguments...) 
# Function required for classes to initialize objects
# self: object being created that gives its identity
# self.attribute = attribute to access the attributes of our object

class Animal(object):
  # Generates a class for animals
  def __init__(self, name):
    self.name = name

## Instantiating objects: to access objects attributes
# Create a Square class with an atrribute sides
class Square(object):
  def __init__(self):
    self.sides = 4
# Outside the class, define a new instance Square
my_shape = Square()
# and access the attribute with the dot notation
print my_shape.sides

class Animal(object):
  # Generates a class for animals
  def __init__(self, name):
    self.name = name

zebra = Animal("Jeffrey")
print zebra.name

## self attribute is only used on __init__() function
# Class definition
class Animal(object):
  """Makes cute animals."""
  # For initializing our instance objects
  def __init__(self, name, age, is_hungry):
    self.name = name
    self.age = age
    self.is_hungry = is_hungry

# Note that self is only used in the __init__()
# function definition; we don't need to pass it
# to our instance objects.

zebra = Animal("Jeffrey", 2, True)
giraffe = Animal("Bruce", 1, False)
panda = Animal("Chad", 7, True)

print zebra.name, zebra.age, zebra.is_hungry
print giraffe.name, giraffe.age, giraffe.is_hungry
print panda.name, panda.age, panda.is_hungry

## Class scope (global, member, instance variables/functions)
# Global: Variables available everywhere
# Member: Variables only available to members of a class
# Instance: Variables available to particular instances of class

# is_alive is a member_variable for all the elements of Animal()
class Animal(object):
  """Makes cute animals."""
  is_alive = True
  def __init__(self, name, age):
    self.name = name
    self.age = age

zebra = Animal("Jeffrey", 2)
giraffe = Animal("Bruce", 1)
panda = Animal("Chad", 7)

print zebra.name, zebra.age, zebra.is_alive
print giraffe.name, giraffe.age, giraffe.is_alive
print panda.name, panda.age, panda.is_alive

## Methods: Functions inside a class (like __init__())
# Define the description method/function inside the class
class Animal(object):
  """Makes cute animals."""
  is_alive = True
  def __init__(self, name, age):
    self.name = name
    self.age = age
  # Add your method here!
  def description(self):
    print self.name
    print self.age

hippo = Animal("Theodore", 3)
hippo.description()

## A class can have any number of member variables
# They will be available to all memebers of a class
# Create 2 instances of an animal
hippo = Animal("Jake", 12)
cat = Animal("Boots", 3)
# Ask for one of the variables
print hippo.is_alive
# Change that variable
hippo.is_alive = False
# Check for what animal changed
print hippo.is_alive
print cat.is_alive

class Animal(object):
  """Makes cute animals."""
  is_alive = True
  health = "good"
  def __init__(self, name, age):
    self.name = name
    self.age = age
  # Add your method here!
  def description(self):
    print self.name
    print self.age

hippo = Animal("Theodore", 3)
hippo.description()

sloth = Animal("Viriato", 6)
ocelot = Animal("Kurt", 2)

print hippo.health
print sloth.health
print ocelot.health

## Example of real class: ShioppingCart
class ShoppingCart(object):
  """Creates shopping cart objects
  for users of our fine website."""
  items_in_cart = {}
  def __init__(self, customer_name):
    self.customer_name = customer_name

  def add_item(self, product, price):
    """Add product to the cart."""
    if not product in self.items_in_cart:
      self.items_in_cart[product] = price
      print product + " added."
    else:
      print product + " is already in the cart."

  def remove_item(self, product):
    """Remove product from the cart."""
    if product in self.items_in_cart:
      del self.items_in_cart[product]
      print product + " removed."
    else:
      print product + " is not in the cart."

my_cart = ShoppingCart("Geralt")
my_cart.add_item("Witcher Sword", 200)

## Inheritance: Process by which one class takes on the attributes
# and methods of another to express a relationship
# Ex: A Panda is a bear so it will inherit from bear class

class Customer(object):
  """Produces objects that represent customers."""
  def __init__(self, customer_id):
    self.customer_id = customer_id

  def display_cart(self):
    print "I'm a string that stands in for the contents of your shopping cart!"

class ReturningCustomer(Customer):
  """For customers of the repeat variety."""
  def display_order_history(self):
    print "I'm a string that stands in for your order history!"

monty_python = ReturningCustomer("ID: 12345")
monty_python.display_cart()
monty_python.display_order_history()

## Inheritance syntax: 
# class DerivedClass(BaseClass):
  # code goes here

class Shape(object):
  """Makes shapes!"""
  def __init__(self, number_of_sides):
    self.number_of_sides = number_of_sides

# Add your Triangle class below!
class Triangle(Shape):
  def __init__(self, side1, side2, side3):
    self. side1 = side1
    self. side2 = side2
    self. side3 = side3

## Override from the parents class
class Employee(object):
  def __init__(self, name):
    self.name = name
  def greet(self, other):
    print "Hello, %s" % other.name

class CEO(Employee):
  def greet(self, other):
    print "Get back to work, %s!" % other.name

ceo = CEO("Emily")
emp = Employee("Steve")
emp.greet(ceo)
# Hello, Emily
ceo.greet(emp)
# Get back to work, Steve!

class Employee(object):
  """Models real-life employees!"""
  def __init__(self, employee_name):
    self.employee_name = employee_name

  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 20.00
  
# This class changes the wage of a part time employee
class PartTimeEmployee(Employee):
  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 12.00

# Access to the superclass method (super call)
# m() method derived from the base class
# class Derived(Base):
  # def m(self):
    # return super(Derived, self).m()

class Employee(object):
  """Models real-life employees!"""
  def __init__(self, employee_name):
    self.employee_name = employee_name

  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 20.00

# Add your code below!
class PartTimeEmployee(Employee):
  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 12.00
  
  def full_time_wage(self, hours):
    return super(PartTimeEmployee, self).calculate_wage(hours)

milton = PartTimeEmployee('Milton')
print milton.full_time_wage(10)

## Recap:
class Triangle(object):
  # Member variables
  number_of_sides = 3
  
  # Initialize the class
  def __init__(self, angle1, angle2, angle3):
    self.angle1 = angle1
    self.angle2 = angle2
    self.angle3 = angle3
  
  # Method for checking sum(angles) = 180
  def check_angles(self):
    if (self.angle1 + self.angle2 + self.angle3 == 180):
      return True
    else:
      return False
    
# Instance Triangle class
my_triangle = Triangle(90,30,60)
print my_triangle.number_of_sides
print my_triangle.check_angles()

# Inheritance
class Equilateral(Triangle):
  # Member variable
  angle = 60
  def __init__(self):
    self.angle1 = self.angle
    self.angle2 = self.angle
    self.angle3 = self.angle
