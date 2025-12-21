# Python functions are treated as first class citizens

print("------------------------------------------------------")
"""
1. A function can take one or more functions as parameters 
2. A function can be returned as a result of another function  3. A function can be modified 
4. A function can be assigned to a variable 
"""

def sum_numbers(nums):
    return sum(nums)

def higher_order_function(f, lst):
    summation = f(lst)
    return summation

sum_nums = higher_order_function(sum_numbers, [1,2,3,4,5])
print("Sum nums: ", sum_nums)
print("------------------------------------------------------")

def square(num):
    return num**2

def cube(num):
    return num**3

def absolute_value(num):
    if num<0:
        return num*-1
    return num

def higher_order_function_powers(fun_type):
    if fun_type=='square':
        return square
    elif fun_type=='cube':
        return cube
    elif fun_type=='absolute':
        return absolute_value
    else:
        return f"No function defined for this type {fun_type}"

square_hof = higher_order_function_powers('square')
cube_hof = higher_order_function_powers('cube')
abs_hof = higher_order_function_powers('absolute')

print("Square: ",square_hof, square_hof(5))
print("Cube: ", cube_hof, cube_hof(3))
print("Abs: ", abs_hof, abs_hof(-4))
print("------------------------------------------------------")

def add_ten():
    ten = 10
    def add(num):
        return ten+num
    return add
closure_add = add_ten()
print("Add five: ",closure_add(5))
print("Add ten: ",closure_add(10))
print("Add twentyfive: ", closure_add(15))

print("------------------------------------------------------")

def greeting():
    return 'Welcome to Python'

def uppercase_decorator(func):
    def wrapper():
        fun = func()
        make_upper = fun.upper()
        return make_upper
    return wrapper

greet = uppercase_decorator(greeting)
print("Greeting: ", greet())


print("------------------------------------------------------")

'''
This decorator function is a higher order function
that takes a function as a parameter
'''

def upper_case_decorators(function):
    def wrapper():
        func = function()
        make_upper = func.upper()
        return make_upper
    return wrapper

@upper_case_decorators
def greeting_decorator():
    return 'Python decorators are good'

print("Greeting decorators: ", greeting_decorator())


print("------------------------------------------------------")

def split_decorators(function):
    def wrapper():
        func = function()
        make_split = func.split()
        return make_split
    return wrapper

@split_decorators
@upper_case_decorators
def upper_split_dec():
    return 'Python split upper decorators'

print("Upper case split decorators: ", upper_split_dec())

print("------------------------------------------------------")

def decorator_with_params(function):
    def wrapper_params(param1, param2):
        function(param1, param2)
        print(f"My first name is {param1}")
    return wrapper_params

@decorator_with_params
def full_name(first_name, last_name):
    print("I am {} {}. I love to teach.".format(first_name, last_name))

print("Decor with params: ", full_name('Vicky','Madhu'))



print("------------------------------------------------------")

# Some are higher order functions are built in
# map
# filter
# reduce

# lambda function can be passed as a parameter

# map(function, iterable)

numbers = [1,2,3,4,5,6,7,8,9,10]
def square(x):
    return x**2

num_squares = map(square, numbers)
print("Map HOF squares: ", list(num_squares))

num_cube = map(lambda x: x**3, numbers)
print("Map HOF cube: ", list(num_cube))

num_to_str = map(str, numbers)
print("Num to str: ", list(num_to_str))

even_numbers = filter(lambda x:x%2==0, numbers)
print("HOF Even numbers: ", list(even_numbers))

odd_numbers = filter(lambda x: x%2==1, numbers)
print("HOF odd numbers: ", list(odd_numbers))

num_to_tuple = map( lambda i: (i, i**2), numbers)
print("Num to tuple: ", list(num_to_tuple))


print("------------------------------------------------------")

names = ['Vicky','Madhu','Python','JavaScript','Medical']

def change_upper(name):
    return name.upper()

names_upper = map(change_upper, names)
print("Names upper: ", list(names_upper))

names_upper_lambda = map(lambda name: name.upper(), names)
print("Names upper lambda: ", list(names_upper_lambda))


long_names = filter(lambda name: len(name)>5, names)
print("Long names: ", list(long_names))

import functools

reduce_total = functools.reduce(lambda x,y:x+" "+y, names)
print("Reduce Total: ", reduce_total)

reduce_sum = functools.reduce(lambda x,y: x + y, numbers)
print("Reduce sum: ", reduce_sum)