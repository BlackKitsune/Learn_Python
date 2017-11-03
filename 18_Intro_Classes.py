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


