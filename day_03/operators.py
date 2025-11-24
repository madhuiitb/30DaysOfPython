age = 24
height = 5.6
store = 1+4j
base = input("Enter base")
triangle_height = input("Enter triangle height")
area = 0.5 * float(base) * float(triangle_height)
print("The area of the triangle is ",area)

side_a=input("Enter side a: ")
side_b=input("Enter side b: ")
side_c=input("Enter side c: ")

perimeter = side_a+side_b+side_c
print("The perimeter of the triangle is ",perimeter)

rectangle_length=input("Enter rectangle length: ")
rectangle_width=input("Enter rectangle width: ")

rectangle_area = float(rectangle_length)*float(rectangle_width)
rectangle_perimeter = 2*(rectangle_length+rectangle_width)

print("The rectangle area and perimeter: ",rectangle_area, rectangle_perimeter)

pi=3.14
circle_radius=input("Enter circle radius: ")
circle_area = float(circle_radius) * float(circle_radius) * float(pi)
circle_circumference = 2*float(pi)*float(circle_radius)

print("The circle area and circumference: ", circle_area, circle_circumference)

#y=2x-2
#y=mx+b
m=2
b=-2
y=-2
x=1

y3= 10-2
x3= 6-2
s_m=y3/x3
print("Comparing slopes: ",m==s_m)
print("Comparing slopes: ",m!=s_m)
print("Comparing slopes: ",m<s_m)
print("Comparing slopes: ",m>s_m)
print("Comparing slopes: ",m>=s_m)
print("Comparing slopes: ",m<=s_m)

print("Compare lengths: ", len('python')!=len('dragon'))
print("And operator: ", 'on' in 'python' and 'on' in 'dragon')

print("Jargon: ", 'jargon' in 'I hope this course is not full of jargon')
print("No on", 'on' not in 'python' and 'on' not in 'dragon')

len_python = len('python')
len_float = float(len_python)
len_str = str(len_float)

print("Convert len->float->str: ", len_python, len_float, len_str)

n=10
print("divisible by 2: ", n%2==0)

floor_value = int(2.7)
print("floor division: ",floor_value==7//3)

print("type of 10: ", type(10)==type('10'))

print("9.8 equal to 10", int(9.8)==10)


