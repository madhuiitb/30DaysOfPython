print("Hello World")
# print 'hello world' // Syntax Error
# print(age) // Name Error
age=25
print(age)

numbers = [1,2,3,4,5]
# print(numbers[5]) IndexError
print(numbers[4])


# import maths : ModuleNotFoundError
import math
# print(math.PI) AttributeError: module 'math' has no attribute 'PI'
print(math.pi)


users = {'name':'Madhu', 'age':25, 'country':'India'}
print(users['name'])
# print(users['county']) KeyError: 'county'
print(users['country'])

# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(5+'4')
print(5 + int('4'))
print(4+float('3'))

# ImportError: cannot import name 'power' from 'math'
# from math import power

from math import pow
print(pow(2,3))

# ValueError: invalid literal for int() with base 10: '12a'
# print(int('12a'))


#ZeroDivisionError: division by zero
# print(1/0)

