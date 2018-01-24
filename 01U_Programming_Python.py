#++++++++++++ PROGRAMMING WITH PYTHON ++++++++++++++++++++++

### FUNCTIONS ++++++++++++++++++++++++++++++++++++++++++++++

### TAKE A BREAK
# Program that plays your favorite song every two hours
# to force you to make a break while working

# Repeat 3x:
#       1. Wait 2 hrs
#       2. Open a browser

# Import all necessary libraries
import time
import webbrowser

total_breaks = 1
break_count = 0

# Start to count with the current time time.ctime()
print("This program started on " + time.ctime())

# Reapeat 3 times
while (break_count < total_breaks):
    # Wait for a number of seconds
    time.sleep(7200)
    # Open the browser
    webbrowser.open("https://www.youtube.com/watch?v=ngzC_8zqInk")
    # Increase the counter
    break_count = break_count + 1
    
    

### SECRET MESSAGE

# Programm that rename a group of files
# Step 1: Get all the files names
# Step 2: For each file: rename the files
# Step 3: Take care of Exceptions

import os
from string import maketrans

def rename_files():
    #(1) get file names from a given folder
    # Take the content of the folder into a list
    # os.listdir(r"D:\examples") for window machine
    file_list = os.listdir("D:/examples")
    print(file_list)

    # Debugging Error: The system cannot find the file
    saved_path = os.getcwd()     # current working directory
    print("Current Working Directory is " + saved_path)
    # change the working directory
    os.chdir("D:/examples")

    #(2) rename each file inside the folder
    for file_name in file_list:
        print("Old Name - " + file_name)
        print("New name - " + file_name.maketrans(None, "0123456789"))
        os.rename(file_name, file_name.maketrans(None, "0123456789"))
        
rename_files()

### CLASES ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

## DRAW SQUARE +++++++++++++++++++++++++++++++++++++
# Draw art with Python

# Draw by thinking how the turtle will move
# Inside turtle library, there is a class Turtle
# CLASS is a box with properties inside that start
# with __init__ function

import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)


def draw_art():
    # Open a window to draw on it
    window = turtle.Screen()
    window.bgcolor("red")

    # Create an instance of the class Turtle
    # with turtle shape, color yellow...
    # Brad and Angie will be instances of the class
    # The class is the blueprint of a building
    # The instance are the characteristics of that
    # blueprint

    # Create the turtle Brad - Draws a square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
    draw_square(brad)

    # Create the turtle Angie - Draws a circle
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

    # Create the turtle triangle - Draws a triangle
    triangle = turtle.Turtle()
    triangle.shape("turtle")
    triangle.color("black")
    # Move the turtle forward a distance
    sides = 3
    count = 1
    while (count <= sides):
        triangle.backward(100)
        triangle.right(120)
        count += 1

    # Close the window on a click
    window.exitonclick()

# draw_art()

def draw_square_art():
    window = turtle.Screen()
    window.bgcolor("red")
    # Create the turtle Brand - Draw a circle with square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)

    for i in range(1,37):
        draw_square(brad)
        brad.right(10)

    window.exitonclick()

draw_square_art()

## DRAW A FLOWER
import turtle

def draw_flower():
    window = turtle.Screen()
    window.bgcolor("white")

    # Create the turtle ifg - Draw flower
    ifg = turtle.Turtle()
    ifg.shape("turtle")
    ifg.color("black")
    ifg.speed(20)

    # Draw flower
    for i in range(36):
        for side in range(2):
            ifg.forward(100)
            ifg.right(60)
            ifg.forward(100)
            ifg.right(120)
        ifg.right(10)
    ifg.right(90)
    ifg.forward(350)

    window.exitonclick()

draw_flower()

## SEND A TEXT MESSAGE
# Send text messages toyour phone number
# Using twilio external librarie

# from twilio.rest import TwilioRestClient
from twilio import rest
# client is a class of TwilioRestClient winth a phone number

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AAcd59kd0lw90ow2kejoiwujeoiu"
auth_token = "faie49jrlwkjeosklejwk"
client = rest.TwilioRestClient(account_sid, auth_token)

message = client.sms.messages.create(
    body = "My name is Isabel",
    to = "+34678665544",         # Replace with your phone number
    from_ =  "+34678923456")     # Replace with your Twilio number
print(message.sid)

## PROFANITY EDITOR
# Programm that checks for bad words and sends
# a message of alert
# Built in functions like open() will be used
# You don't need to import any library
# open() returns and object of file type

import urllib

# (1) Read text
# (2) Check the text for curse words

# (1) Read text
def read_text():
    quotes = open("C:/detect_profanity/movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()

# (2) Check the text for curse words
# we will use the curse file search www.WDYL.com from google
# http://www.wdylike.appspot.com/?q=shit the word at the end
# It will take false if no bad words are found
# connection will be an instance of the file like object

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check)
    output = connection.read()
    if "true" in output:
        print("Profanity Alert!!")
    elif "false" in output:
        print("This document has no curse words!!")
    else:
        print("Could not scan the document properly")
    connection.close()

read_text()

### CREATE YOUR OWN CLASSES ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## MOVIE WEBSITE
# Programm that opens a website created by us
# Plays the trailer for each movie in the website
# For conventions for programmers from google:
# https://google.github.io/styleguide/pyguide.html

# (1) Create a class of movie for each instance
# When defining clases first capital letter
class Movie():
    # __init__() is the class constructor function
    # self is the instance being created
    def __init__(self, movie_title, movie_storyline, poster_image, trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer
      
# (2) show_trailer function that show the trailer
    def show_trailer(self, ):
        webbrowser.open(self.trailer_youtube_url)

# Programm to create the webpage with the data base
# Define an array with the movies in the data base
movies = [toy_story, avatar, interstellar]

(...)

## DATA BASE FOR MOVIE
# File in the same folder as media.py
# In this file we define the list of movies
import media

toy_story = media.Movie("Toy Story",
                        "A Story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on a alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

print(avatar.storyline)

interstellar = media.Movie("Interstellar",
                           "A man saves humanity travelling in space - time",
                           "https://en.wikipedia.org/wiki/File:Interstellar_film_poster.jpg",
                           "https://www.youtube.com/watch?v=2LqzF5WauAw")

print(interstellar.storyline)
interstellar.show_trailer()


## CLASS VARIABLES
# Instance Variables: In the class "Movie" there are IV like title, storyline, poster_image...
# We want to create variables with the same values for all the instances

# Ex: This is the possible valid ratings for all movies in the data base defined at the level
# of the class and outside of the init

# (1) Create a class of movie for each instance
# When defining clases first capital letter
class Movie():
    # _doc_ variable will have the documentation inside """
    """ This class provides a way to store movie related information """

    # Define the CLASS variable for the class movie
    # If it is going to be constant --> With capital letters
    VALID_RATINGS = ['G', 'PG', 'PG_13', 'R']
    
    # __init__() is the class constructor function
    # self is the instance being created
    def __init__(self, movie_title, movie_storyline, poster_image, trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer
      
# (2) show_trailer function that show the trailer
    def show_trailer(self, ):
        webbrowser.open(self.trailer_youtube_url)
        
# (3) Data base for the movie on another file
import media

toy_story = media.Movie("Toy Story",
                        "A Story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on a alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

interstellar = media.Movie("Interstellar",
                           "A man saves humanity travelling in space - time",
                           "https://en.wikipedia.org/wiki/File:Interstellar_film_poster.jpg",
                           "https://www.youtube.com/watch?v=2LqzF5WauAw")

print(media.Movie.VALID_RATINGS)
print(meida.Movie.__doc__)
        
# In python all classes come with a kind of prexisting variables like _doc_
# _doc_ will give the documentation of a class
turtle.Turtle._doc_
print(meida.Movie.__doc__)  # for the Movies class
print(media.Movie.__name__)  # Name of the class (Movies)
Print(media.Movie.__module__)  # Name of the module in which this class was defined (media)

## INHERITANCE: Classes that inherit some variables from the parent class to the child class
# inheritance.py
class Parent():
    def __init__(self):
    # Print that tell us every time the parent class is called
    print("Parent constructor called")
        self.last_name = last_name
        self.eye_color = eye_color

# class_name (inheritance_class) will inheritance all the variables
class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child contructor called")
        self.number_of_toys = number_of_toys

# Elements of the class go in another file
billy_cyrus = Parent("Cyrus", "blue")
print(billy_cyrus.last_name)

miley_cyrus = Child("Cyrus", "Blue", 5)
print(miley_cyrus.last_name)  # will print Cyrus
print(miley_cyrus.number_of_toys)  # will print 5

# Output:
#Child constructor called
#Parent constructor called
#Cyrus
#5

# Note: Use inheritance with the Movies and a new TvShow() from a Video() parent class
class Video():
    - title
    - duration
 
 class Movie(Video)  # Inherits variables from Video() class
    - storyline
    - poster_image
    - youtube_trailer
    
    def show_trailer()
    
 class TVShow(Video):  # Inherits variables from Video() class
    - season
    - episode
    - tv_station
    
    def get_local_listing()
 
# Use inheritance
class Parent():
    def __init__(self):
    # Print that tell us every time the parent class is called
    print("Parent constructor called")
        self.last_name = last_name
        self.eye_color = eye_color
    
    def show_info(self):
        print("Last Name - "+self.last_name)
        print("Eye color - "+self.eye.color)

class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child contructor called")
        self.number_of_toys = number_of_toys
    
    def show_info(self):
        print("Last Name - "+self.last_name)
        print("Eye color - "+self.eye.color)
        print("Number of colors - '+self.number_of_toys)

# Elements of the class go in another file
billy_cyrus = Parent("Cyrus", "blue")
miley_cyrus = Child("Cyrus", "Blue", 5)

billy_cyrus.show_info()  # print name and eye color directly
miley.cyrus.show_info()  # print name and eye color inheritance from parent class

# Once the same show_info is created in the class Child it will use the
# show_info 

miley.cyrus.show_info()  # print name, eye color and number of toys from Child





