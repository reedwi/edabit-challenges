import datetime
import math
import operator
import numpy as np
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
def sort_by_length1(lst):
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

#You need to create two functions to substitute str() and int(). A function called int_to_str() that converts integers into strings and a 
# function called str_to_int() that converts strings into integers.
def int_to_str(num):
    num1 = f"'{num}'"
    print(num1)
    return num1
	

def str_to_int(num):
    num = num[1:-1]
    return num

#Write a function that stutters a word as if someone is struggling to read it. The first two letters are repeated twice with an 
# ellipsis ... and space after each, and then the word is pronounced with a question mark ?.
def stutter(word):
    two = word[:2]
    stutter = f'{two}... {two}... {word}?'
    return stutter
    print(stutter)

# The vertical bar | is the equivalent to "or" in RegEx. The regular expression x|y matches either "x" or "y". Write the regular expression 
# that will match all red flag and blue flag in a string. You must use | in your expression. Flags can come in any order.
import re

txt1 = "red flag blue flag"
txt2 = "yellow flag red flag blue flag green flag"
txt3 = "pink flag red flag black flag blue flag green flag red flag"
pattern = "red flag|blue flag"

# print(re.findall(pattern, txt3))

#Create a function that takes a list of non-negative integers and strings and return a new list without the strings.
def filter_list(lst):
    int_lst = []
    for value in lst:
        if isinstance(value, int) == True:
            int_lst.append(value)
    return int_lst

# Create a function that takes a string and returns the number (count) of vowels contained within it.
def count_vowels(txt):
    vowels = 'aeiouAEIOU'
    return sum(letter in vowels for letter in txt)

# Christmas Eve is almost upon us, so naturally we need to prepare some milk and cookies for Santa! Create a function that accepts
#  a Date object and returns True if it's Christmas Eve (December 24th) and False otherwise
def time_for_milk_and_cookies(date):
    if date.strftime('%m') == '12' and date.strftime('%d') == '24':
        return True
    else:
        return False

# Create a function that returns the number of arguments it was called with.
def num_args(*args):
    return(len(args))

# Write a function that searches a list of names (unsorted) for the name "Bob" and returns the location in the list. If Bob is not in the list, return -1.
def find_bob(names):
    while names:
        try:
            x = names.index('Bob')
            return x
        except ValueError:
            return -1      

# Create a function to convert a list of percentages to their decimal equivalents.
def convert_to_decimal(perc):
    perc = [p.strip() and p.replace('%', '') for p in perc]
    perc = [float(p) for p in perc]
    perc = [p/100 for p in perc]
    print(perc)
    return perc

# convert_to_decimal(["1%", "2%", "3%"])
# convert_to_decimal(["33%", "98.1%", "56.44%", "100%"])

# Create a function that reverses a boolean value and returns the string "boolean expected" if another variable type is given.
def reverse(arg):
    if type(arg) == bool:
        if arg == False:
            print(True)
            return True
        elif arg == True:
            print(False)
            return False
    else:
        print('boolean expected')
        return 'boolean expected'

# Write a function that finds the sum of the first n natural numbers. Make your function recursive.
def sum_numbers(n):
    if n <= 1:
        return n
    else:
        return n + sum_numbers(n-1)
        
# Given a list of numbers and a value n, write a function that returns the probability of choosing a number 
# greater than or equal to n from the list. The probability should be expressed as a percentage, rounded to one decimal place.
def probability(lst, n):
    amount = []
    for num in lst:
        if num >= n:
            amount.append(num)
    prob = round(100 * (len(amount)/len(lst)), 1)
    return prob

# probability([1, 4, 18, 19, 15, 3, 3, 11], 23)

# Create a function that returns True if a given inequality expression is correct and False otherwise.
def correct_signs(txt):
    return eval(txt)

# Write a function that takes a list of elements and returns only the integers.
def return_only_integer(lst):
    ints = [value for value in lst if type(value) == int]
    return ints

# Programmer Pete is trying to turn two lists inside one list into one without messing the order of the list nor the type and 
# because he's pretty advanced he made it without blinking but I want you to make it too.
def one_list(lst):
    lst = [v for val in lst for v in val]
    return lst

# Create a function that takes a list of strings and return a list, sorted from shortest to longest.
def sort_by_length(lst):
    lst.sort(key=len)
    return lst

# Create a function that takes a single character as an argument and returns the char code of its lowercased / uppercased counterpart.
def counterpartCharCode(char):
    if char.isalpha() == True and char.isupper():
        return ord(char.lower())
    elif char.isalpha() == True and char.islower():
        return ord(char.upper())
    elif char.isalpha() == False:
        return ord(char)

# Write a function that creates a dictionary with each (key, value) pair being the (lower case, upper case) versions of a letter, respectively.
def mapping(letters):
    dct = {letters[i]:letters[i].upper() for i in range(len(letters))}
    print(dct)
    return dct

# Write a function that takes a credit card number and only displays the last four characters. The rest of the card number must be replaced by ************.
def card_hide(card):
    last4 = card[-4:]
    last4 = last4.rjust(len(card), '*')
    return last4

# A typical car can hold four passengers and one driver, allowing five people to travel around. Given n number of people, return how many cars are needed to seat everyone comfortably.
def cars_needed(n):
    return math.ceil(n/5)

# The insurance guy calls again and apologizes. They found another policy made by your spouse, but this one is limited to cover a particular maximum in losses (for example, 50,000€). You send a bill to your spouse for the difference you lost.
# Given an dict of the stolen items and a limit, return the difference between the total value of those items and the limit of the policy.
def calc_diff(obj, limit):
    return sum(obj.values()) - limit

# Create a function that takes a number as an argument and returns "Fizz", "Buzz" or "FizzBuzz".

# If the number is a multiple of 3 the output should be "Fizz".
# If the number given is a multiple of 5, the output should be "Buzz".
# If the number given is a multiple of both 3 and 5, the output should be "FizzBuzz".
# If the number is not a multiple of either 3 or 5, the number should be output on its own as shown in the examples below.
# The output should always be a string even if it is not a multiple of 3 or 5.
def fizz_buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return 'FizzBuzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    else:
        return '{}'.format(num)

# Write a function that removes any non-letters from a string, returning a well-known film title.
def letters_only(txt):
    txt = re.sub("[^a-zA-Z]+", "", txt)
    return txt

# Imagine a messaging device with only one button. For the letter A, you press the button one time, for E, you press it five times, for G, it's pressed seven times, etc, etc.

# Write a function that takes a string (the message) and returns the total number of times the button is pressed.
import string
def how_many_times(msg):
    num = [string.ascii_lowercase.index(letter) + 1 for letter in msg]
    return sum(num)

# Write a function that takes a list and a number as arguments. Add the number to the end of the list, then remove the first element of the list. The function should then return the updated list.
def next_in_line(lst, num):
    if not lst:
        return 'No list has been selected'
    else:
        lst.append(num)
        lst.pop(0)
        return lst

# Create a function that takes a string and returns a string with its letters in alphabetical order.
def alphabet_soup(txt):
    return ''.join(sorted(txt))

# Create a function that takes a list of numbers between 1 and 10 (excluding one number) and returns the missing number.
def missing_num(lst):
    # lst.append(0)
    return 55 - sum(lst)

# Write a function that returns the lexicographically first and lexicographically last rearrangements of a string. Output the results in the following manner:
def first_and_last(s):
    lst = []
    first = ''.join(sorted(s))
    last = ''.join(sorted(s, reverse=True))
    lst.append(first)
    lst.append(last)
    return lst

# This Triangular Number Sequence is generated from a pattern of dots that form a triangle. The first 5 numbers of the sequence, or dots, are:
# This means that the first triangle has just one dot, the second one has three dots, the third one has 6 dots and so on.

# Write a function that gives the number of dots with its corresponding triangle number of the sequence.
def triangle(n):
    num = n * (n+1)/2
    return int(num)

# /You are stuck in a multi-storey car parking lot. Your task is to exit the carpark using only the staircases. Exit is always at the bottom right of the ground floor.

# Create a function that takes a two-dimensional list where:

# Free carparking spaces are represented by a 0
# Staircases are represented by a 1
# Your starting position is represented by a 2 and can be at any level of the car park.
# Exit is always at the bottom right of the ground floor.
# You must use the staircases (1) to go down a level.
# Each floor will have only one staircase apart from the ground floor which will not have any staircases.
# ... and returns a list of the quickest route out of the carpark.
def parking_exit(lst):
    res = []
    pos = -1
    for row in lst:
        if pos < 0 and 2 in row:
            pos = row.index(2)
        if pos > -1 and 1 in row:
            stair = row.index(1)
            diff = stair - pos
            if diff > 0:
                res.append("R{}".format(diff))
                res.append("D1")
                pos = stair
            elif diff < 0:
                res.append("L{}".format(-diff))
                res.append("D1")
                pos = stair
            else:
                res[-1] = "D{}".format(int(res[-1][1]) + 1)
        elif 1 not in row:
            ext = len(row) - 1
            diff = ext - pos
            if diff > 0:
                res.append("R{}".format(diff))
            elif diff < 0:
                res.append("L{}".format(-diff))
    return res


# Create a function that takes a string and returns True or False, depending on whether the characters are in order or not.
def is_in_order(txt):
    sort = sorted(txt)
    if list(txt) == sort:
        print(True)
        return True
    else:
        print(False)
        return False

# I am trying to filter out empty arrays from an array. In other words, I want to transform something that looks like this: 
# ["a", "b", [], [], [1, 2, 3]] to look like ["a", "b", [1, 2, 3]]. My code looks like this:
def remove_empty_arrays(arr):
		return [x for x in arr if x != []]


# Create a function that returns the sum of all even elements in a 2D matrix.
def sum_of_evens(lst):
    return sum([y for x in lst for y in x if y % 2 == 0])

# Create a function that takes a list and finds the integer which appears an odd number of times.
def find_odd(lst):
    for num in lst:
        if lst.count(num) % 2 != 0:
            return num

# Create a function that takes two numbers and a mathematical operator + - / * and will perform a calculation with the given numbers.
def calculator(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Can't divide by 0!"
        else:
            return num1 / num2

# Create a function, that will for a given a, b, c, do the following:

# Add a to itself b times.
# Check if the result is divisible by c.
def abcmath(a, b, c):
    num = a*b
    print(num)
    if num % c == 0:
        return True
    else:
        return False

# There are two types of graphs; directed and undirected. In an undirected graph, the edges between nodes have no particular 
# direction (like a two-way street) whereas in a directed graph, each edge has a direction associated with it (like a one-way street).
# For two nodes in a graph to be considered adjacent to one another, there must be an edge between them. In the example given above, 
# nodes 0 and 1 are adjacent, but nodes 0 and 2 are not.
# We can encode graphs using an adjaceny matrix. An adjacency matrix for a graph with "n" nodes is an "n * n" matrix where the entry at 
# row "i" and column "j" is a 0 if nodes "i" and "j" are not adjacent, and 1 if nodes "i" and "j" are adjacent.
# https://edabit.com/challenge/3DAkZHv2LZjgqWbvW
def is_adjacent(matrix, node1, node2):
    if matrix[node1][node2] == 1:
        return True
    else: return False


# Create a function that takes damage and speed (attacks per second) and returns the amount of damage after a given time.
def damage(damage, speed, time):
    if time == 'second' and damage > 0 and speed > 0:
        return damage * speed
    elif time == 'minute' and damage > 0 and speed > 0:
        return damage * speed * 60
    elif time == 'hour' and damage > 0 and speed > 0:
        return damage * speed * 60 * 60
    else:
        return 'invalid'

def XO(txt):
    txt = txt.lower()
    x_count = txt.count('x')
    o_count = txt.count('o')
    if o_count == x_count:
        return True
    else:
        return False

# Create a function that takes a string and returns a string in which each character is repeated once.
def double_char(txt):
    return ''.join([l * 2 for l in txt])

# Given a list of numbers, write a function that returns a list that...

# Has all duplicate elements removed.
# Is sorted from least to greatest value
def unique_sort(lst):
    new_lst = list(dict.fromkeys(lst))
    new_lst.sort()
    return new_lst

# Create the function that takes a list of dictionaries and returns the sum of people's budgets.
def get_budgets(lst):
    budgets = [x['budget'] for x in lst]
    return sum(budgets)

# Create a function that returns the list of numbers from a given range. But for multiples of three, return 
# “Eda” instead of the number and for the multiples of five, return “Bit”. For numbers which are multiples of both three and five, return “EdaBit”.
def eda_bit(start, end):
    lst = []
    for val in range(start, end+1):
        if val % 3 == 0 and val % 5 == 0:
            lst.append('EdaBit')
        elif val % 3 == 0:
            lst.append('Eda')
        elif val % 5 == 0:
            lst.append('Bit')
        else:
            lst.append(val)
    return lst

# Create a function that takes the height and radius of a cone as arguments and returns the volume of the cone rounded to the nearest hundredth. 
# See the resources tab for the formula.
def cone_volume(h, r):
    return round(((1/3) * math.pi * (r**2) * h), 2)

# The Code tab has code which attempts to add a clone of a list to itself. There is no error message, but the results are not as intended. Can you fix the code?
def clone(lst):
    lst.append(lst[:])
    return lst

# Create a function that returns True if the given string has any of the following:

# Only letters and no numbers.
# Only numbers and no letters.
# If a string has both numbers and letters, or contains characters which don't fit into any category, return False
def alphanumeric_restriction(s):
    if s.isdigit() == True:
        return True
    elif s.isalpha() == True:
        return True
    else:
        return False

# Additional spaces have been added to a sentence. Return the correct sentence by removing them. All words should be separated by one space, and there should 
# be no spaces at the beginning or end of the sentence.
def correct_spacing(sentence):
    sentence.strip()
    return " ".join(sentence.split())

# Create a function that takes a string as input and capitalizes a letter if its ASCII code is even and returns its lower case version if its ASCII code is odd.
def ascii_capitalize(txt):
    new = []
    for val in txt:
        if ord(val) % 2 == 0:
            new.append(val.upper())
        else:
            new.append(val.lower())
    return ''.join(new)

# Check the principles of minimalist code in the intro to the first challenge.

# In the Code tab you will find a code that is missing a single character in order to pass the tests. However, your goal is to submit a function as minimalist as possible. Use the tips in the tips section below.

# Write a function that returns the strings:

# "both" if both given booleans a and b are True.
# "first" if only a is True.
# "second" if only b is True .
# "neither" if both a and b are False.
def are_true(a, b):
    if a == True and b == True:
        return 'both' 
    elif a == True and b == False:
        return 'first' 
    elif a == False and b == True:
        return 'second' 
    else: return 'neither' 

# A set is a collection of unique items. A set can be formed from a list from removing all duplicate items.
def setify(lst):
    new = list(set(lst))
    new.sort()
    return new

# Create a function that returns the thickness (in meters) of a piece of paper after folding it n number of times. The paper starts off with a thickness of 0.5mm.
def num_layers(n):
    val = 0.5*2**n/1000
    return '{}m'.format(val)

# Create a function that takes a number as an argument and returns True or False depending on whether the number is 
# symmetrical or not. A number is symmetrical when it is the same as its reverse.
def is_symmetrical(num):
    newstr = str(num)
    new = newstr[::-1]
    if newstr == new:
        return True
    else: return False

# A snail goes up the stairs. Every step, he must go up the step, then go across to the next step. He wants to reach the top of the tower.

# Write a function that returns the distance the snail must travel to the top of the tower given the height and length of each step and the height of the tower.
def total_distance(height, length, tower):
    return round(tower/height * (height+length), 1)

# A salesman has a number of cities to visit. They want to calculate the total number of possible paths they could take, visiting each city once before returning home. 
# Return the total number of possible paths a salesman can travel, given n cities.

# If we have cities A, B and C, possible paths would be:
def paths(n):
    return math.factorial(n)

# Count the amount of ones in the binary representation of an integer. For example, since 12 is 1100 in binary, the return value should be 2.
def count_ones(num):
    binary = bin(num)
    return int(str(binary).count('1'))

# Write a function that retrieves the last n elements from a list.
def last(a, n):
    if n == 0:
        return []
    elif len(a) + 1 < n or a == []:
        return 'invalid'
    else:
        return a[-n:]

# Create a function that takes two strings and returns either True or False depending on whether they're anagrams or not.
def is_anagram(s1, s2):
    sort1 = sorted(s1.lower())
    print(sort1)
    sort2 = sorted(s2.lower())
    print(sort2)
    if sort1 == sort2:
        return True
    else:
        return False

# Create a function that moves all capital letters to the front of a word.
def cap_to_front(s):
    upper = [char for char in s if char.isupper()]
    lower = [char for char in s if char.islower()]
    return ''.join(upper)+''.join(lower)

# Create a function to calculate how many characters in total are needed to make up the shape. 
# You will be given a list of strings which make up a shape in the compiler (i.e. a square, a rectangle or a line).
def count_characters(lst):
    return len([x for val in lst for x in val])
    return sum(len(i) for i in lst)

# Create a function that takes a single string as argument and returns an ordered list containing the indices of all capital letters in the string.
def index_of_caps(word):
    return [word.index(char) for char in word if char.isupper()]

# Using list comprehensions, create a function that finds all even numbers from 1 to the given number.
def find_even_nums(num):
    return [n for n in range(1, num+1) if n % 2 == 0]

# Create a function that returns a base-2 (binary) representation of a base-10 (decimal) string number. 
# To convert is simple: ((2) means base-2 and (10) means base-10) 010101001(2) = 1 + 8 + 32 + 128.

# Going from right to left, the value of the most right bit is 1, now from that every bit to the left will be x2 the value, 
# value of an 8 bit binary numbers are (256, 128, 64, 32, 16, 8, 4, 2, 1).
def binary(d):
	return bin(d)[2:]

# Create a function that counts the number of times a particular letter shows up in the word search.
def letter_counter(lst, letter):
    return sum([row.count(letter) for row in lst])

# Create a function that takes a variable number of arguments, each argument representing the number of items in a group, 
# and returns the number of permutations (combinations) of items that you could get by taking one item from each group.
def combinations(*items):
    result = 1
    for x in items:
        if x == 0:
            result = result*1
        else:
            result = result*x
    return result

# Return the sum of all items in a list, where each item is multiplied by its index (zero-based). For empty lists, return 0.
def index_multiplier(lst):
    return sum([i*x for i, x in enumerate(lst)])

# Create a function that converts two lists of x- and y- coordinates into a list of (x, y) coordinates.
def convert_cartesian(x, y):
    return [[coordx, y[i]] for i, coordx in enumerate(x)]

# A museum wants to get rid of some exhibitions. Katya, the interior architect, comes up with a plan to remove the most boring exhibitions. 
# She gives them a rating, and removes the one with the lowest rating. Just as she finishes rating the exhibitions, she's called off to an important meeting. 
# She asks you to write a program that tells her the ratings of the items after the lowest one is removed.

# Create a function that takes a list of integers and removes the smallest value.
def remove_smallest(lst):
    if lst:
        srtd = sorted(lst)
        lst.remove(srtd[0])
    return lst

# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits. 
# Your task is to create a function that takes a string and returns True if the PIN is valid and False if it's not.
def is_valid_PIN(pin):
    if len(pin) in (4, 6) and pin.isdigit():
        return True
    else: return False

# A financial institution provides professional services to banks and claims charges from the customers based on the number of man-days provided. 
# Internally, it has set a scheme to motivate and reward staff to meet and exceed targeted billable utilization and revenues by paying a bonus for 
# each day claimed from customers in excess of a threshold target.

# This quarterly scheme is calculated with a threshold target of 32 days per quarter, and the incentive payment for each billable day in excess of such 
# threshold target is shown as follows:
# Please note that incentive payment is calculated progressively. As an example, if an employee reached total billable days of 45 in a quarter, 
# his/her incentive payment is computed as follows:
def bonus(days):
    if days <= 32:
        return 0
    elif 40 >= days > 32:
        return (days - 32) * 325
    elif 48 >= days > 40:
        return (8 * 325) + (550 * (days-40))
    else:
        return (8 * 325) +  (8 * 550) + (600 * (days-48))

# Given a list of scrabble tiles (as dictionaries), create a function that outputs the maximum possible score a player can achieve by summing up the total number of points 
# for all the tiles in their hand. Each hand contains 7 scrabble tiles.
def maximum_score(tile_hand):
    return sum([x['score'] for x in tile_hand])

# Given a list of numbers, create a function which returns the list but with each element's index in the list added to itself. 
# This means you add 0 to the number at index 0, add 1 to the number at index 1, etc...
def add_indexes(lst):
    return [lst[i] + i for i, n in enumerate(lst)]

# A number n is automorphic if n^2 ends in n.

# For example: n=5, n^2=25

# Create a function that takes a number and returns True if the number is automorphic, False if it isn't.
def is_automorphic(n):
    n2 = n ** 2
    l = len(str(n))
    if n == 0:
        return True
    print(str(range(n2)[-1] + 1)[-l:] == str(n) )
    return str(range(n2)[-1] + 1)[-l:] == str(n) 

    return str(n**2).endswith(str(n))

# Create a function that calculates the missing value of 3 inputs using Ohm's law. The inputs are v, r or i (aka: voltage, resistance and current).

# Ohm's law: V = R * I

def ohms_law(v, r, i):
    if sum(x is None for x in [v, r, i]) != 1:
        return 'Invalid'
    else:
        if v is None:
            return round(r*i, 2)
        elif r is None:
            return round(v/i, 2)
        elif i is None:
            return round(v/r, 2)

# Given an unsorted list, create a function that returns the nth smallest element (the smallest element is the first smallest, the second smallest element is the second smallest, etc).
# def nth_smallest(lst, n):
# 	if len(lst) < n:
#         return
#     else:
#         lst.sort()
#         return lst[n-1]

# An isogram is a word that has no duplicate letters. Create a function that takes a string and returns either True or False depending on whether or not it's an "isogram".
def is_isogram(txt):
    txt = txt.lower()
    return sum([txt.count(i) for i in txt]) == len(txt)
    return len(txt) == len(set(txt.lower()))

# A group of friends have decided to start a secret society. The name will be the first letter of each of their names, sorted in alphabetical order.

# Create a function that takes in a list of names and returns the name of the secret society.
def society_name(friends):
    return ''.join(sorted(name[0] for name in friends))

# With Python 3, you can assign variables from lists in a much more succinct way. Create variables first, middle and last from the given list using destructuring 
# assignment (check the Resources tab for some examples), where:
first, *middle, last = [1, 2, 3, 4, 5, 6]

# Create a function that takes an integer and returns a list from 1 to the given number, where:

# If the number can be divided evenly by 4, amplify it by 10 (i.e. return 10 times the number).
# If the number cannot be divided evenly by 4, simply return the number.
def amplify(num):
    return [n*10 if n % 4 == 0 else n for n in range(1, num+1)]

# Your task is to create a Circle constructor that creates a circle with a radius provided by an argument. The circles constructed must have two getters getArea() (PIr^2) 
# and getPerimeter() (2PI*r) which give both respective areas and perimeter (circumference).

# For help with this class, I have provided you with a Rectangle constructor which you can use as a base example.
class Rectangle:

	def __init__(self, sideA=0, sideB=0):
		self.sideA = sideA
		self.sideB = sideB

	def getArea(self):
		return self.sideA * self.sideB
  
	def getPerimeter(self):
		return 2 * (self.sideA + self.sideB)

class Circle:

    def __init__(self, radius=0):
        self.radius = radius

    def getPerimeter(self):
        return self.radius * 2 * math.pi

    def getArea(self):
        return self.radius ** 2 * math.pi

# Create a function, that will for a given a, b, c, do the following:

# Add a to itself b times.
# Check if the result is divisible by c.
def abcmath(a, b, c):
    i = 0
    while i <= range(b)[-1]:
        a += a
        i += 1
    else:
        return a % c == 0

    return a*(2**b) % c == 0
    # return (a * b) % c == 0

# Write a function that removes all capitals letters from a sentence except the first letter, put quotation marks around the sentence and add ", whispered Edabit." at the end.
def shhh(txt):
    if txt: return '"{}{}", '.format(txt[0].upper(), txt[1:].lower()) + 'whispered Edabit.'
    else: return '"", whispered Edabit.'

# Create a function that takes a list of numbers and return the number that's unique.

def unique(lst):
    return list(filter(lambda x: lst.count(x) == 1, lst))[0]

# Given a number, return a list containing the two halves of the number. If the number is odd, make the rightmost number higher.
def number_split(n):
    return [math.floor(n/2), math.ceil(n/2)]

# Create a function that returns the mean of all digits.
def mean(num):
    dig_list = list(map(int, str(num)))
    mean = sum(dig_list)/len(dig_list)
    return int(mean)

# Create a function that takes a list of strings and integers, and filters out the list so that it returns a list of integers only.
def filter_list(l):
    return [x for x in l if isinstance(x, int)]

# Create a function that replaces all the vowels in a string with a specified character.
def replace_vowels(txt, ch):
    return re.sub('[aeiou]', ch, txt)

# Create a function that will return an integer number containing the amount of digits in the given integer num.
def num_of_digits(num):
    return len(str(abs(num)))

def total_volume(*boxes):
    return sum([math.prod(x) for x in boxes])

# I'm trying to watch some lectures to study for my next exam but I keep getting distracted by meme compilations, vine compilations, anime, and more on my favorite video platform.

# Your job is to help me create a function that takes a string and checks to see if it contains the following words or phrases:

# "anime"
# "meme"
# "vines"
# "roasts"
# "Danny DeVito"
# If it does, return "NO!". Otherwise, return "Safe watching!".
# I'm trying to watch some lectures to study for my next exam but I keep getting distracted by meme compilations, vine compilations, anime, and more on my favorite video platform.

# Your job is to help me create a function that takes a string and checks to see if it contains the following words or phrases:

# "anime"
# "meme"
# "vines"
# "roasts"
# "Danny DeVito"
# If it does, return "NO!". Otherwise, return "Safe watching!".
def prevent_distractions(txt):
    nope = ('anime', 'meme', 'vine', 'roasts', 'Danny DeVito')
    return 'NO!' if any(i in txt for i in nope) else 'Safe watching!'

# Write a function that takes a string as an argument and returns the left most integer in the string.
def left_digit(num):
    return int(re.search('[0-9]', num).group(0))
   
# Create a function that takes three arguments a, b, c and returns the sum of the numbers that are evenly divided by c from the range a, b inclusive.
def evenly_divisible(a, b, c):
    return sum([x for x in range(a,b+1) if x % c == 0])

# The "Reverser" takes a string as input and returns that string in reverse order, with the opposite case.
def reverse(txt):
    return ''.join([x.lower() if x.isupper() else x.upper() for x in txt[::-1]])
    return txt[::-1].swapcase()

# Mary wants to run a 25-mile marathon. When she attempts to sign up for the marathon, she notices the sign-up sheet doesn't directly state the marathon's length. 
# Instead, the marathon's length is listed in small, different portions. Help Mary find out how long the marathon actually is.

# Return True if the marathon is 25 miles long, otherwise, return False.
def marathon_distance(d):
    return sum([abs(x) for x in d]) == 25

# Create a function that takes in a current mood and return a sentence in the following format: "Today, I am feeling {mood}". 
# However, if no argument is passed, return "Today, I am feeling neutral".
def mood_today(mood='neutral'):
    if mood: return 'Today, I am feeling {}'.format(mood)
    else: return 'Today, I am feeling neutral'

# Create a function that takes three parameters where:

# x is the start of the range (inclusive).
# y is the end of the range (inclusive).
# n is the divisor to be checked against.
# Return an ordered list with numbers in the range that are divisible by the third parameter n. Return an empty list if there are no numbers that are divisible by n.
def list_operation(x, y, n):
    return [z for z in range(x, y+1) if z % n == 0]

# Write a function that returns the number of users in a chatroom based on the following rules:

# If there is no one, return "no one online".
# If there is 1 person, return "user1 online".
# If there are 2 people, return user1 and user2 online".
# If there are n>2 people, return the first two names and add "and n-2 more online".
# For example, if there are 5 users, return:
def chatroom_status(users):
    if not users:
        return 'no one online'
    elif len(users) == 1:
        return '{} online'.format(users[0])
    elif len(users) == 2:
        return '{} and {} online'.format(users[0], users[1])
    elif len(users) > 2:
        return '{}, {} and {} more online'.format(users[0], users[1], len(users)-2)

# Create a function that determines whether each seat can "see" the front-stage. A number can "see" the front-stage if it is strictly greater than the number before it.

# Everyone can see the front-stage in the example below:
# FRONT STAGE
# [[1, 2, 3, 2, 1, 1],
# [2, 4, 4, 3, 2, 2],
# [5, 5, 5, 5, 4, 4],
# [6, 6, 7, 6, 5, 5]]

# Starting from the left, the 6 > 5 > 2 > 1, so all numbers can see.
# 6 > 5 > 4 > 2 - so all numbers can see, etc.
def can_see_stage(seats):
    # print(list(map(list, zip(*seats))))
    # transposed_list = np.array(seats).T.tolist()
    # t_f = [True if val == sorted(val) and val == list(set(val)) else False for val in transposed_list]
    # print(t_f)
    # print(sum(t_f))
    # print(len(t_f))
    # if sum(t_f) == len(t_f):
    #     return True
    # else: return False
	seats = np.array(seats)
	return np.all(seats[1:] - seats[:-1] > 0)


	return all(sorted(set(row)) == list(row) for row in zip(*seats))


# Given two integers a and b, return how many times a can be halved while still being greater than b.
def halve_count(a, b):
	i=0
	while a>b:
		a = a/2
		i+=1
	return i-1

# Suppose that you invest $10,000 for 10 years at an interest rate of 6% compounded monthly. What will be the value of your investment at the end of the 10 year period?

# Create a function that accepts the principal p, the term in years t, the interest rate r, and the number of compounding periods per year n. The function returns
#  the value at the end of term rounded to the nearest cent.

# For the example above:

# compound_interest(10000, 10, 0.06, 12) ➞ 18193.97
# Note that the interest rate is given as a decimal and n=12 because with monthly compounding there are 12 periods per year. Compounding can also be done annually, quarterly, weekly, or daily.
def compound_interest(p, t, r, n):
    return round(p * (1 + (r/n))**(n*t), 2)

# Create a class Employee that will take a full name as argument, as well as a set of none, one or more keywords. Each instance 
# should have a name and a lastname attributes plus one more attribute for each of the keywords, if any.
# class Employee(name):
#     def __init__(self, name, lastname, salary=int(), height=int(), nationality='', subordinates=[]):
#         self.name = name
#         self.lastname = lastname
#         self.salary = salary
#         self.height = height
#         self.nationality = nationality
#         self.subordinates = subordinates

#     name = Employee(name.name, name.lastname)
#     print(name)

# In this challenge, you have to convert a weight weighed on a planet of the Solar System to the corresponding weight on another planet.

# To convert the weight, you have to divide it by the gravitational force of the planet on which is weighed and multiply the result (the mass) for the gravitational force of the other planet. See the table below for a list of gravitational forces:

# weight on planet_a / gravitational force of planet_a * gravitational force of planet_b
def space_weights(planet_a, weight, planet_b):
    weightdict = {
        'Mercury'	: 3.7,
        'Venus' : 8.87,
        'Earth' : 9.81,
        'Mars' : 3.711,
        'Jupiter' : 24.79,
        'Saturn' : 10.44,
        'Uranus' : 8.69,
        'Neptune' : 11.15
    }
    return round(weight/weightdict[planet_a] * weightdict[planet_b], 2)

# Create a function which returns a list of booleans, from a given number. Iterating through the number one digit at a time, append True if the digit is 1 and False if it is 0.
def integer_boolean(n):
    return [int(x) == 1 for x in n]

# Create a function that returns True if an asterisk * is inside a box.
def in_box(lst):
    another_lst = []
    for val in lst:
        val = ''.join(val.split())
        val = val.strip('*')
        print(list(val))
        srt = sorted(val)
        if '*' in val and list(val) != srt:
            another_lst.append(1)
    if len(another_lst) > 0:
        print(len(another_lst))
        return True
    else: return False


# Write a function that returns True if the binary string can be rearranged to form a string of alternating 0s and 1s.
def can_alternate(s):
    if s.count('0') == s.count('1') or s.count('0') - s.count('1') == 1 or s.count('0') - s.count('1') == -1:
        return True
    else: return False


# Create a function that takes a list of numbers or strings and returns a list with the items from 
# the original list stored into sublists. Items of the same value should be in the same sublist.
def advanced_sort(lst):
    result = {}
    for x in lst:
        if not result.get(x):
            result[x] = [x]
        else:
            result[x].append(x)

    dic_lst = list(result.values())
    return sorted(dic_lst, key= lambda x: lst.index(x[0]))
        
