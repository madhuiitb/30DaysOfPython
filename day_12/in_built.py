import os
print('-----------------------------------------------------')
print("# Creating a directory")
os.mkdir('person_dict_4')

print('-----------------------------------------------------')
print("# Changing the current directory")

# os.chdir('day_12/path')

print('-----------------------------------------------------')
print("# Getting current working directory")
os.getcwd()

print('-----------------------------------------------------')
print("# Removing directory")
# os.rmdir('person_dict')
# os.rmdir('person_dict_3')
# os.rmdir('person_dict_2')
os.rmdir('person_dict_4')


print('-----------------------------------------------------')
print("# SYS")
import sys
#print(sys.argv[0], argv[1], sys.argv[2])
print('Welcome {}. Enjoy {} challenge!'.format(sys.argv[1],sys.argv[2]))
print(sys)
# sys.exit() # to exit sys

sys.maxsize
sys.path
sys.version

print('-----------------------------------------------------')
print("# STATISTICS")

from statistics import *
ages = [20,20,4,24,25,22,26,20,23,22,26]

print("Mean:- ",mean(ages))
print("Median:- ",median(ages))
print("Mode:- ",mode(ages))
print("Stdev:- ",stdev(ages))

print('-----------------------------------------------------')
print("# Math Modules")

import math
print("PI {}".format(math.pi))
print("Square root:- ", math.sqrt(2))
print("power function:- ", math.pow(2,3))
print("Round to the lowest:- ", math.floor(9.81))
print("Round to the highest:- ", math.ceil(9.81))
print("Logarithm with 10 as base:- ", math.log10(100))
print("Logarithm with 10 as base:- ", math.log(10,10))
print("Exponential function:- ",math.exp(1))

# from math import pi
# print(pi)
# ----------------------------------
# from math import pi, sqrt, pow, floor, ceil, log10
# print(pi)
# print(sqrt(2))
# print(pow(2,3))
# print(floor(9.81))
# ----------------------------------
# from math import *
# print(pi)
# print(sqrt(2))
# print(pow(2,3))
# ----------------------------------
# from math import pi as PI
# print(PI)

print('-----------------------------------------------------')
print("# String Modules")

import string
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.punctuation)

print('-----------------------------------------------------')
print("# Random Modules")

from random import randint, random
print(randint(10,60))
print(random())
