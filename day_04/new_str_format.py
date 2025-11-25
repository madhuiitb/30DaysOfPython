first_name = "Vicky"
last_name ="Madhu"

language ="Python"

format_str="I am {} {}. I am learning {}".format(first_name,last_name,language)
print(format_str)

a=4
b=3

print("{}+{}={}".format(a,b,a+b))
print("{}-{}={}".format(a,b,a-b))
print("{}*{}={}".format(a,b,a*b))
print("{}/{}={:.2f}".format(a,b,a/b))

# Strings and numbers

radius = 10
pi=3.14
area = pi*radius**2

format_strings = "The area of circle with a radius {} is {:.3f}".format(radius,area)
print(format_strings)
