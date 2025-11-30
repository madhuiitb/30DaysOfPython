print("-----------------------------------------------------")
print("Accessing elements in sets")
print("Check item in sets")
print("-----------------------------------------------------")

fruits = {'apple','banana','orange','lemon'}
print(fruits)
print("Does set fruits contain orange?", 'orange' in fruits)


print("-----------------------------------------------------")
print("Adding item to set using add(): method")
print("-----------------------------------------------------")
fruits.add("goa")
fruits.add("mango")
fruits.add("pineapple")

print(fruits)

print("-----------------------------------------------------")
print("Adding item to set using update(): method")
print("-----------------------------------------------------")
vegetables = {'tomoto', 'potato','cabbage'}
print(vegetables)

fruits.update(vegetables)
print(fruits)

print("-----------------------------------------------------")
print("Removing item to set using remove(): method")
print("-----------------------------------------------------")

fruits.remove("apple")
print(fruits)


print("-----------------------------------------------------")
print("Removing item to set using pop(): method")
print("-----------------------------------------------------")

removed_element = fruits.pop()
print("Random element:", removed_element)
remove_another_element = fruits.pop()
print("Random element:", remove_another_element)


print("-----------------------------------------------------")
print("Clearning items from set using clear(): method")
print("-----------------------------------------------------")
vegetables.clear()
print(vegetables) # set() empty set definition


print("-----------------------------------------------------")
print("Deleting set using del key")
print("-----------------------------------------------------")
del vegetables

print("-----------------------------------------------------")
print("Converting list to set")
print("-----------------------------------------------------")

veg_list = ['tomoto', 'potato','cabbage','bottle gourd']
veg_set = set(veg_list)

print(veg_set) # Random order, bacause set is unorder