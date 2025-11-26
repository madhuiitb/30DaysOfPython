print("-----------------------------------------")
print("#Slicing Items from a List Positive Indexing")
print("-----------------------------------------")
fruits = ["apple", "banana", "cherry",'mango','orange']
all_fruits = fruits[0:5]
three_fruits = fruits[0:3]
all_fruits_one= fruits[0:]
print(all_fruits)
print(three_fruits)
print(all_fruits_one)

banana_cherry = fruits[1:3]
cherry_mango_orange = fruits[2:]
print(banana_cherry)
print(cherry_mango_orange)

every_2nd = fruits[::2] # ski 1 item
print(every_2nd)
every_3rd = fruits[::3] #it skips 2 items
print(every_3rd)

print("-----------------------------------------")
print("#Slicing Items from a List Negative Indexing")
print("-----------------------------------------")

all_fruits_negative = fruits[-5:]
banana_cherry_negative = fruits[-4:-2]
reverse_all_fruits = fruits[::-1]
print(all_fruits_negative)
print(banana_cherry_negative)
print(reverse_all_fruits)