print("-------------------------------------------------------")
print("Function with parameters part-1")
print("-------------------------------------------------------")

def greets(name):
    message = name + ", welcome to Python for Everyone!"
    return message
print(greets("Hello"))

def add_ten(num):
    ten=10;
    return num+10
print(add_ten(12))

def square_number(num):
    square = num**2
    return square
print(square_number(5))

def area_of_circle(radius):
    PI = 3.14
    area = PI*radius**2
    return area
print(area_of_circle(5))


def sum_numbers(num):
   total = 0
   for i in range(num+1):
       total += i
   return total
print(sum_numbers(10))