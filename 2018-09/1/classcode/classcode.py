"""
    Pylab 1 Sept 2018

    "List, For-Loops and Dictionaries"

    Nathan @nate_somewhere

    Class notes:

    Python3 required, python2 not guaranteed to work completely
    Internet connection required
    Text editor required
"""

# print('hello world')
#
# # Comments in python use a '#'

## WARM UP QUIZ

# PART I
a = 5
b = 5.0
c = a / 2
d = b / 2

# What is type(a)?

# What is type(b)?

# What is c?

# What is d?


# PART II

e = [a, b]
f = range(10)

# What is type(e)?
# What is len(e)?
# What is type(f)?
# What are the contents of f?
# What is 'range' called?
# How do I get help on 'range'?


# LISTS
# https://docs.python.org/3/tutorial/introduction.html#lists

# list slicing [start:end:stride]

weekdays = ['mon','tues','wed','thurs','fri']
weekdays[0]         # element 0
weekdays[0:3]       # elements 0, 1, 2
weekdays[:3]        # elements 0, 1, 2
weekdays[-1]        # last element

test = weekdays[3:]        # elements 3, 4

weekdays

weekdays[-2]        # last element (element 4)
weekdays[::2]       # every 2nd element (0, 2, 4)
weekdays[::-1]      # backwards (4, 3, 2, 1, 0)

days = weekdays + ['sat','sun']     # concatenate lists

days_appended = ['mon','tues','wed','thurs','fri']
days_appended.append('sat') # append individual elements to list
days_appended.append('sun')

#########
# Exercise - Lists
#########

# How do I slice out 'wed'?
# How do I check the type of 'mon'?
# How do I slice out 'wed' through 'friday'?
# What are two ways to slice out 'fri'?
# What is the length of days and days_appended?
# How do I reverse the order of days? (hint: google it)



## FOR LOOPS AND BASIC LIST COMPREHENSIONS

# print 1 through 5
nums = range(1, 6)
for num in nums:
    pass # pass does nothing in loop
    # print(num)

# for loop to create a list of cubes
cubes = []
for num in nums:
    cubes.append(num**3)

# equivalent list comprehension
cubes = [num**3 for num in nums]    # [1, 8, 27, 64, 125]


# EXERCISE:
# Given that: letters = ['a','b','c']
# Write a for-loop that returns: ['A','B','C']
# Write a list comprehension that returns: ['A','B','C']
# Hint: 'hello'.upper() returns 'HELLO'


# BONUS EXERCISE:
# Given that: word = 'abc'
# Write a list comprehension that returns: ['A','B','C']



## LIST COMPREHENSIONS WITH CONDITIONS

nums = range(1, 6)

# for loop to create a list of cubes of even numbers
cubes_of_even = []
for num in nums:
    if num % 2 == 0:
        cubes_of_even.append(num**3)

# equivalent list comprehension
# syntax: [expression for variable in iterable if condition]

cubes_of_even = [num**3 for num in nums if num % 2 == 0]    # [8, 64]



## DICTIONARIES

# dictionaries are similar to lists:
# - both can contain multiple data types
# - both are iterable
# - both are mutable

# dictionaries are different from lists:
# - dictionaries are unordered*
# - dictionary lookup time is constant regardless of dictionary size

# dictionaries are like real dictionaries:
# - dictionaries are made of key-value pairs (word and definition)
# - dictionary keys must be unique (each word is only defined once)
# - you can use the key to look up the value, but not the other way around

# create a dictionary (and open Variable Explorer in Spyder)
family = {'dad':'homer', 'mom':'marge', 'size':6}

# examine a dictionary
# family[0]           # throws an error (there is no ordering)
family['dad']       # returns 'homer'
len(family)         # returns 3
family.keys()       # returns list: ['dad', 'mom', 'size']
family.values()     # returns list: ['homer', 'marge', 6]
family.items()      # returns list of tuples:
                    #   [('dad', 'homer'), ('mom', 'marge'), ('size', 6)]

# modify a dictionary
family['cat'] = 'snowball'          # add a new entry
family['cat'] = 'snowball ii'       # edit an existing entry
del family['cat']                   # delete an entry
family['kids'] = ['bart', 'lisa']   # value can be a list

# accessing a list element within a dictionary
family['kids'][0]   # returns 'bart'

# EXERCISE:
# Given that: d = {'a':10, 'b':20, 'c':[30, 40]}
# First, print the value for 'a'
# Then, change the value for 'b' to be 25
# Then, change the 30 to be 35
# Finally, append 45 to the end of the list that contains 35 and 40
