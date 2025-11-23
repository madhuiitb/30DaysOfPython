# Day 02: 30 Days of python programming

first_name="Software"
last_name="Engineer"
full_name="Software Engineer"
country="India"
city="Hyderabad"
age=20
year=2020
is_married=False
is_true=True
is_light_on=False
frontend, backend, full_stack, experience = "React.js", "Python", "Next.js", 40

print("First name type: ",type(first_name))
print("Last name type: ",type(last_name))
print("Full name type: ",type(full_name))
print("Country type: ",type(country))
print("City type:", type(city))
print("Age type: ", type(age))
print("Year type: ", type(year))
print("Is married type: ", type(is_married))
print("is true type: ",type(is_true))
print("frontend type: \nbackend type: \nfull_stack type: \nexperience type:", type(frontend),type(backend),type(full_stack),type(experience))


print(len(first_name))
print(first_name==last_name)
num_one=5
num_two=4
total=num_one+num_two
diff=num_two-num_one
product=num_one*num_two
division=num_one/num_two
remainder=num_one%num_two
exp=num_one**num_two
floor_div=num_one//num_two
radius = 30
area_of_circle= float(radius*2*3.14)
circum_of_circle= float(area_of_circle*3.14)
user_radius = input("Enter radius: ")
area = float(int(user_radius)*2*3.14)

f_n = input("Enter the first name: ")
l_n = input("Enter the last name: ")
age = input("Enter the age: ")
country = input("Enter the country: ")

print("User input value: ",f_n,l_n,age,country)