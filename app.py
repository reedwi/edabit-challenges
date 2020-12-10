import datetime
import math
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

https://edabit.com/challenge/PbDLFCa4qp5knYN43
