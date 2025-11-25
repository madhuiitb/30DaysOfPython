# % percentage operator
# %s - String
# %d - Integers
# %f - Floating point numbers
# %.noOfdigits - floating point numbers with fixed precision

first_name="Vicky"
last_name="Madhu"
language="Python"

formatted_string = "I am %s %s. I am learning %s" %(first_name, last_name, language)
print(formatted_string)


# Strings and numbers
radius = 10
pi = 3.14
area = pi*radius**2
formatted_string_numbers = "The area of circle with a radius %d is %.2f." %(radius, area)

python_libraries = ['Django', 'Flask', 'NumPy','Matplotlib', 'Pandas']
formatted_strings = 'The following are python libraries: %s' %(python_libraries)

print(formatted_strings)
