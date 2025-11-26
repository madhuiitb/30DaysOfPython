from traceback import print_tb

print("-----------------------------------------")
print("#Modifying Items")
print("-----------------------------------------")
fruits = ["apple", "mango", "orange","banana", "cherry"]
fruits[0] = "goa"
print(fruits)

fruits[1] = "apple"
print(fruits)

last_index = len(fruits) - 1
fruits[last_index] = 'mango'

print(fruits)

print("-----------------------------------------")
print("#Checking Items")
print("-----------------------------------------")

does_banana_exists = "banana" in fruits
print(does_banana_exists)

does_lime_exists = "lime" in fruits
print(does_lime_exists)


print("-----------------------------------------")
print("#Adding Items")
print("-----------------------------------------")

lst = list()
lst.append("apple")
print(lst)

fruits.append("avacado")
print(fruits)
fruits.append("lime")
print(fruits)


print("-----------------------------------------")
print("#Inserting Items")
print("-----------------------------------------")

lst_inst = ['item1', 'item2']
lst_inst.insert(0,'item0')
print(lst_inst)

fruits.insert(1,'apples')
fruits.insert(2,'bananas')
print(fruits)

print("-----------------------------------------")
print("#Removing Items using remove(): method")
print("-----------------------------------------")

fruits.remove('apples')
fruits.remove('bananas')
print(fruits)


print("-----------------------------------------")
print("#Removing Items using pop(): method")
print("-----------------------------------------")

fruits.pop()
fruits.pop(0)
print(fruits)

print("-----------------------------------------")
print("#Removing Items using del(): method")
print("-----------------------------------------")
# syntax
#del lst[index] # for single item
#del lst # full list delete

del fruits[0]

print(fruits)

del fruits[-1]
print(fruits)

fruits.append("apple")
fruits.append("banana")
fruits.append("cherry")
print(fruits)
del fruits[::2]
print(fruits)

del fruits[1:3]
print(fruits)

#del fruits  ---> NameError: name 'fruits' is not defined
#print(fruits)--> NameError: name 'fruits' is not defined
print("-----------------------------------------")
print("#Clearing Items")
print("-----------------------------------------")

fruits.clear()
print(fruits) # []