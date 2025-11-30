


print("-----------------------------------------------------")
print("Joining sets")
print("-----------------------------------------------------")
fruits = {'apple','banana','orange','lemon'}
veg_set = {'tomoto', 'potato','cabbage','bottle gourd'}
joined_sets = fruits.union(veg_set)
print(joined_sets)

print("-----------------------------------------------------")
print("Joining sets Updated()")
print("-----------------------------------------------------")
fruit_set = {'apple','banana','orange','lemon'}
veg_set.update(fruit_set)
print(veg_set)

print("-----------------------------------------------------")
print("Joining sets intersection()")
print("-----------------------------------------------------")

fruit_set.intersection_update(fruits)
print(fruit_set)

print("-----------------------------------------------------")
print("Checking subset and superset issubset() issuperset()")
print("-----------------------------------------------------")
whole_numbers = {0,1,2,3,4,5,6,7,8,9,10}
even_numbers={0,2,4,6,8,10}
odd_numbers = {1,3,5,7,9}

even_nums_subset = whole_numbers.issubset(even_numbers)
print("Even numbers subset? ",even_nums_subset)
even_nums_superset = whole_numbers.issuperset(even_numbers)
print("Even numbers superset? ",even_nums_superset)

print("-----------------------------------------------------")
print("Checking difference between sets")
print("-----------------------------------------------------")

st1 ={'item1','item2','item3'}
st2={'item1','item2'}

diff_st2 = st2.difference(st1) # s2-s1
diff_st1 = st1.difference(st2) # s1-s2
print(diff_st2) # set()
print(diff_st1) # item3

diff_even_nums = whole_numbers.difference(even_numbers)
print("Even numbers diff? ",diff_even_nums)

print("-----------------------------------------------------")
print("Finding symmetric difference between sets")
print("-----------------------------------------------------")

# (A/B)U(B/A)
symmetric_st1 = st1.symmetric_difference(st2)
print("Symmetric numbers diff? ",symmetric_st1)

symmetric_st2 = st2.symmetric_difference(st1)
print("Symmetric numbers diff? ",symmetric_st2)

print("-----------------------------------------------------")
print("Disjoint sets")
print("-----------------------------------------------------")

disjoint_sets = st1.isdisjoint(st2)
print(disjoint_sets)

disjoint_numbers = even_numbers.isdisjoint(odd_numbers)
print(disjoint_numbers)