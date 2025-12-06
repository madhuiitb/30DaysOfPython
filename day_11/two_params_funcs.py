print("-------------------------------------------------------")
print("Function with two parameters part-1")
print("-------------------------------------------------------")
def generate_full_name(first_name,last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name("Vicky","Madhu"))


def sum_two_numbers(num1,num2):
    total = num1 + num2
    return total
print(sum_two_numbers(1,2))

print("-------------------------------------------------------")
print("Passing arguments with key and value")
print("-------------------------------------------------------")

def print_full_name(first_name,last_name):
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
    return full_name
print(print_full_name(first_name = "Vicky", last_name = "Madhu"))


def is_even(num):
    if num%2==0:
        return True
    return False
print(is_even(21))


def find_even_numbers(num):
    even_numbers = []
    for i in range(1, num+1):
        if is_even(i):
            even_numbers.append(i)
    return even_numbers
print(find_even_numbers(10))


print("-------------------------------------------------------")
print("Function with default parameters")
print("-------------------------------------------------------")

def greet_user(first_name="Vicky"):
    message = "Hello " + first_name
    return message
print(greet_user())
print(greet_user("Madhu"))
