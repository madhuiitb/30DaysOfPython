print("-----------------------------------------")
print("#Copying list using copy(): method ")
print("-----------------------------------------")
fruits = ["apple", "banana", "cherry","goa","mango"]
print(fruits)

fruits_copy= fruits.copy()
print(fruits_copy)

print("-----------------------------------------")
print("#Joining lists using + : operator ")
print("-----------------------------------------")
positive_numbers = [1,2,3,4,5]
zero= [0]
negative_numbers = [-5,-4,-3,-2,-1]

integers = negative_numbers + zero + positive_numbers
print(integers)

vegetables = ["Tomoto",'Onion','Cabbage','Carrot']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)

print("-----------------------------------------")
print("#Joining lists using extend() : method ")
print("-----------------------------------------")
num1 = [1,2,3]
num2 = [4,5,6]
num3 = [7,8,9]

num1.extend(num2)
print(num1)

neg_numbers = [-5,-4,-3,-2,-1]
pos_numbers = [1,2,3,4,5]

neg_numbers.extend(zero)
neg_numbers.extend(pos_numbers)
print(neg_numbers)

print("-----------------------------------------")
print("#Counting Items using count(): method ")
print("-----------------------------------------")

print(fruits.count("apple"))
ages = [22,19,24,22,24,25,22]
print(ages.count(22))

print("-----------------------------------------")
print("#Find index Items using index(): method ")
print("-----------------------------------------")
print(fruits.index("apple"))
print(ages.index(24)) # first occurance

print("-----------------------------------------")
print("#Reversing Items using reverse(): method ")
print("-----------------------------------------")
fruits.reverse()
print(fruits)
ages.reverse()
print(ages)

print("-----------------------------------------")
print("#Sorting Items using sort(): method ")
print("-----------------------------------------")
fruits.sort()
ages.sort()
print(ages)
print(fruits)
ages.sort(reverse=True)
fruits.sort(reverse=True)
print(ages)
print(fruits)