# Create a function that takes a list of numbers lst, a string s and return a list of numbers as per the following rules:

# "Asc" returns a sorted list in ascending order.
# "Des" returns a sorted list in descending order.
# "None" returns a list without any modification.
def asc_des_none(lst, s):
    if s == 'Asc':
        lst.sort()
        return lst
    if s == 'Des':
        lst.sort(reverse=True)
        return lst
    if s == 'None':
        return lst

# print(asc_des_none([0, 1, 2, 3, 4], 'Des'))

# Given three arguments ⁠— a dictionary obj, a key name and a value ⁠— return a dictionary with that name and value in it (as key-value pairs).
def add_name(obj, name, value):
    obj[name] = value
    return obj

# In this challenge, establish if a given integer num is a Curzon number. If 1 plus 2 elevated to num is exactly divisible by 1 plus 2 multiplied by num, then num is a Curzon number.

# Given a non-negative integer num, implement a function that returns True if num is a Curzon number, or False otherwise.
def is_curzon(num):
    first = 2**num + 1
    second = 2*num + 1
    return True if first % second == 0 else False

# Create a function that returns a list of strings sorted by length in ascending order.
def sort_by_length(lst):
    asc_list = sorted(lst, key=len)
    return asc_list

# Create a function that takes in two lists and returns True if the second list follows the first list by one element, and False otherwise. 
# In other words, determine if the second list is the first list shifted to the right by 1.
def simon_says(lst1, lst2):
    for num, ind in enumerate(lst1, start=1):
        if num == 0:
            continue
        if lst2[num] != lst1[num-1]:
            return False
        else :
            return True
    #BETTER
    if lst1[:-1]==lst2[1:]:
        return True
    else:
        return False

# Create a function that takes an integer and returns the factorial of that integer. That is, the integer multiplied by all positive lower integers.
def factorial(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial = factorial*i
    return factorial

# Luke Skywalker has family and friends. Help him remind them who is who. Given a string with a name, return the relation of that person to Luke.

# Person	Relation
# Darth Vader	father
# Leia	sister
# Han	brother in law
# R2D2	droid
def relation_to_luke(name):
    if name == 'Darth Vader':
        return 'Luke, I am your father.'
    if name == 'Leia':
        return 'Luke, I am your sister.'
    if name == 'Han':
        return 'Luke, I am your brother in law.'
    if name == 'R2D2':
        return 'Luke, I am your droid.'

# Create a function that takes a dictionary of student names and returns a list of student names in alphabetical order.
def get_student_names(students):
    values = [v for k, v in students.items()]
    values.sort()
    return values

# Create a function that takes date in the format yyyy/mm/dd as an input and returns "Bonfire toffee" if the date is October 31, else return "toffee".
def halloween(dt):
    if dt.find('10/31', 5) != -1:
        return 'Bonfire toffee'
    else:
        return 'toffee'

# Create a function that takes a string (will be a person's first and last name) and returns a string with the first and last name swapped.
def name_shuffle(txt):
    names = txt.split()
    reverse = f'{names[1]}' + ' ' + f'{names[0]}'
    return reverse

#Count the amount of ones in the binary representation of an integer. For example, since 12 is 1100 in binary, the return value should be 2.
def count_ones(num):
    nums = [int(i) for i in str(bin(num)[2:])]
    return nums.count(1)

