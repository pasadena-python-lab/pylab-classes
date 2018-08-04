"""
Getting Started with Python - Warm Up with Loops and Lists
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
# https://docs.python.org/3/tutorial/introduction.html#numbers

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



# STRINGS - Part II

# concatenate strings
s3 = 'The meaning of life is'
s4 = '42'
s3 + ' ' + s4       # returns 'The meaning of life is 42'
s3 + ' ' + str(42)  # same thing

# split a string into a list of substrings separated by a delimiter

s = 'I like you'
s.split(' ')        # returns ['I','like','you']
s.split()           # same thing


# LISTS
# https://docs.python.org/2/tutorial/introduction.html#lists

nums = [5, 5.0, 'five']     # multiple data types
nums                        # print the list
type(nums)                  # check the type: list
len(nums)                   # check the length: 3
nums[0]                     # print first element
nums[0] = 6                 # replace a list element

nums

nums.append(7)              # list 'method' that modifies the list
# help(nums.append)           # help on this method
# help(nums)
dir(nums) # help on a list object
nums.remove('five')         # another list method

nums

sorted(nums)                # 'function' that does not modify the list
nums                        # it was not affected
nums = sorted(nums)         # overwrite the original list
sorted(nums, reverse=True)  # optional argument

# list slicing [start:end:stride]
weekdays = ['mon','tues','wed','thurs','fri']
weekdays[0]         # element 0
weekdays[0:3]       # elements 0, 1, 2
weekdays[:3]        # elements 0, 1, 2
test = weekdays[3:]        # elements 3, 4

weekdays

weekdays[-2]        # last element (element 4)
weekdays[::2]       # every 2nd element (0, 2, 4)
weekdays[::-1]      # backwards (4, 3, 2, 1, 0)

days = weekdays + ['sat','sun']     # concatenate lists

days

# FOR LOOPS
# https://docs.python.org/3/tutorial/controlflow.html#for-statements

# range returns a list of integers
list(range(0,3))    # returns [0, 1, 2]: includes first value but excludes second value
list(range(30))    # same thing: starting at zero is the default

num = 0

# simple for loop
for num in range(5):
    pass
    # print(num)

# print each list element in uppercase
fruits = ['apple', 'banana', 'cherry']

upper_fruits = []
for i in range(len(fruits)):
    upper_case = fruits[i].upper()
    upper_fruits.append(upper_case)

better_upper_fruits = []
# better for loop
for fruit in fruits:
    upper_case = fruit.upper()
    better_upper_fruits.append(upper_case)


### Learn More About If Statetments, For Loops and Flow Control
# https://automatetheboringstuff.com/chapter2/


### PRACTICAL EXERCISE - Cleaning / Extracting URLs from 'Messy' Data
# 1. Extract the urls of these craigslist pasadena lists and return them in a list
# Hints: What is the \n? Print it out to see
# What type of data is the variable craigslist_urls? What can you do to turn it into a list?

craigslist_urls = """
<item rdf:about="https://losangeles.craigslist.org/sgv/apa/d/luxury-pasadena-condo/6661685397.html">\n
<item rdf:about="https://losangeles.craigslist.org/sgv/apa/d/spacious-2bd-1ba-in-great/6658896943.html">\n
<item rdf:about="https://losangeles.craigslist.org/sgv/apa/d/beautifully-furnished-1bed/6661669788.html">\n
<item rdf:about="https://losangeles.craigslist.org/sgv/apa/d/room-in-2-bedroom-1bt/6654578054.html">\n
<item rdf:about="https://losangeles.craigslist.org/sgv/apa/d/2-bed-2-bath-with-2-parking/6657589985.html">
"""


# Datasource: https://losangeles.craigslist.org/search/apa?availabilityMode=0&format=rss&query=pasadena
