# Function is a reusable block of code
# To declare function python provides def keyword
# function block code is executed only if the function is called or invoked

print("-------------------------------------------------------")
print("Declaring and calling functions")
print("-------------------------------------------------------")

def function_name():
    print("Sample function")
    print("Code goes here")

function_name()

print("-------------------------------------------------------")
print("Function without parameters")
print("-------------------------------------------------------")

def generate_full_name():
    first_name ='Madhu'
    last_name ='Vicky'
    space=' '
    full_name = first_name + space + last_name
    print(full_name)

generate_full_name()

def add_two_numbers():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)
add_two_numbers()

print("-------------------------------------------------------")
print("Function without parameters part-2")
print("-------------------------------------------------------")

def add_two_number_return():
    num_one = 12
    num_two = 3
    total = num_one + num_two
    return total
print(add_two_number_return())