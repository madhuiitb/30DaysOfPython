# lists can have items of different data types

lst = ['Madhu', 250, True, {"Country":"India", "city":"HYD"}]

#Accessing List items using positive indexing
print("-----------------------------------------")
print("#Accessing List items using positive indexing")
print("-----------------------------------------")

fruits = ['banana', 'apple', 'mango', 'lemon', 'orange']

first_fruit = fruits[0]
second_fruit = fruits[1]
print(first_fruit)
print(second_fruit)

last_index = len(fruits)-1;
last_fruit = fruits[last_index]
print(last_fruit)

print("-----------------------------------------")
print("#Accessing List items using negative indexing")
print("-----------------------------------------")

first_fruit_negative = fruits[-5]
second_fruit_negative = fruits[-4]
print(first_fruit_negative)
print(second_fruit_negative)

last_fruit_negative = fruits[-1]
last_second_fruit_negative = fruits[-2]
last_third_fruit_negative = fruits[-3]

print(last_fruit_negative)
print(last_second_fruit_negative)
print(last_third_fruit_negative)


print("-----------------------------------------")
print("#Unpacking List Items Example: 1")
print("-----------------------------------------")

lst_one = ['item1', 'item2', 'item3', 'item4', 'item5']
first_item,second_item,third_item, *rest = lst_one
print(first_item)
print(second_item)
print(third_item)
print(rest)

print("-----------------------------------------")
print("#Unpacking List Items Example: 2")
print("-----------------------------------------")
first, second, third, *rest,tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)
print(second)
print(third)
print(rest)
print(tenth)


print("-----------------------------------------")
print("#Unpacking List Items Example: 3")
print("-----------------------------------------")

countries = ['Germany','France','Belgium','Switzerland','Italy', 'Denmark','Iceland']
gr,fr,bg,*scandic,ic=countries
print(gr)
print(fr)
print(bg)
print(scandic)
print(ic)