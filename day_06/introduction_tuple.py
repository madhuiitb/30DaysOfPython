print("---------------------------------------------------")
print("Creating Tuple")
print("---------------------------------------------------")
empty_tuple = ()
print(empty_tuple) # ()

#intial values

tpl =("Hello", "World")
print(tpl)
print("---------------------------------------------------")
print("Tuple Length")
print("---------------------------------------------------")
print(len(tpl))

print("---------------------------------------------------")
print("Accessing Tuple values")
print("---------------------------------------------------")

fruits = ("apple", "banana", "cherry", "mango", "orange")
print(fruits)

print("---------------------------------------------------")
print("Accessing Tuple values positive indexing")
print("---------------------------------------------------")
first_fruit = fruits[0]
second_fruit = fruits[1]
last_index = len(fruits) - 1
last_fruit = fruits[last_index]

print(first_fruit)
print(second_fruit)
print(last_fruit)

print("---------------------------------------------------")
print("Accessing Tuple values negative indexing")
print("---------------------------------------------------")

first_fruit_negative = fruits[-5]
second_fruit_negative = fruits[-4]
last_fruit_negative = fruits[-1]
print(first_fruit_negative)
print(second_fruit_negative)
print(last_fruit_negative)

print("---------------------------------------------------")
print("Accessing full tuple values negative indexing")
print("---------------------------------------------------")

full_tuple_fruits= fruits[-4:]
print(full_tuple_fruits) # it starts from -4 fruits



print("---------------------------------------------------")
print("Accessing skipping / slicing tuple values")
print("---------------------------------------------------")

skip_one_fruits= fruits[::-2]
skip_one = fruits[::2]
range_tuple = fruits[1:4]
print(skip_one_fruits) # it starts from -4 fruits
print(skip_one)
print(range_tuple)

print("---------------------------------------------------")
print("changing tuples to lists")
print("---------------------------------------------------")

fruits_list = list(fruits)
print(fruits_list)
fruits_list[0]="lemon"
print(fruits_list)
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)


print("---------------------------------------------------")
print("Checking Item in a tuples")
print("---------------------------------------------------")

print("apple"in fruits_tuple)
print("lemon"in fruits_tuple)
print("lemon"in fruits)


print("---------------------------------------------------")
print("Joining tuples")
print("---------------------------------------------------")
joining_fruits = fruits_tuple + fruits
print(joining_fruits)

print("---------------------------------------------------")
print("Deleting tuples")
print("---------------------------------------------------")
del fruits_tuple


