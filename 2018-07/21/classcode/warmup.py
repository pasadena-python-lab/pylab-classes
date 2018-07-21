"""
Getting Started with Python - Warm Up
Instructor - Nathan Danielsen @nate_somewhere

"""

# print('hello world')
#
# # Comments in python use a '#'
#
# # Exercise: Comments
# print('uncomment me')
# print('thanks for coming on this nice rainy day')
# BASIC DATA TYPES

# Numbers
# https://docs.python.org/2/tutorial/introduction.html#numbers

5  # Integer
5.0  # Float (decimal)
x = 5  # creates an object

y = 2345

type(x)  # check the type: int (not declared explicitly)
type(5)  # assigning it to a variable is not required
type(5.0)  # float
type(True)  # bool

### Exercise: Checking Data Type
text = 'What type of data type am I?'


# math operations

1 + 2  # Addition
7 - 5  # Division
5 * 7  # Multiplication
10 / 3  # Division
10 / 3.0  # Floor division
16 % 5  # Modulo (remainder)
2**10  # Exponent

# variable assignment
a = 1
b = 2
c = 6

### Exercise: A little math
#1 Assign a variable 'd' that equals 'a' plus 'b' minus 'c'

d = a + b -c

#2 What value is d?



#3 Assign a variable 'e' that is 'd' divided by 6.0

e = d / 6.0

#4 what is the value of e?


# STRINGS
# https://docs.python.org/3/tutorial/introduction.html#strings

s = str(42)

s  # convert another data type into a string (casting)
s = 'I like you'

# examine a string
s[0]  # returns 'I'
len(s)  # returns 10

# string slicing like lists
s[0:7]  # returns 'I like'
s[6:]  # returns 'you'
s[-1]  # returns 'u'

# EXERCISE: Book Titles (Part 1)
# 1) Extract the book title from the string
# 2) Save each book title to a variable (ie book1_title)
# 3) How many characters/elements are in each title?

book1 = "Beyond the Door by Dick, Philip K., 1928-1982"

book2 = "The Variable Man by Dick, Philip K., 1928-1982"

book3 = "The Skull by Dick, Philip K., 1928-1982"

## Learn more with Automate the Boring Stuff:
## https://automatetheboringstuff.com/chapter1/


# FUNCTIONS

# A function is like a mini-program within a program.
def hello():
    print('Howdy!')
    print('Howdy!!!')
    print('Hello there.')

# Can you run the function hello()?


def hello_friend(name):
    print('Howdy, ' + name)

# Can you say Howdy to your code buddy?


### Exercise: Can you write a function that:
# Takes in your name and the language you are learning
# Prints out an Introduction for yourself
# Bonus -- if you are learning 'python', then it prints out 'Cool!'
# Hint - google python 'if' statement

### Learn More About Functions
# https://automatetheboringstuff.com/chapter3/

### Learn More About If Statetments and Flow Control
# https://automatetheboringstuff.com/chapter2/
