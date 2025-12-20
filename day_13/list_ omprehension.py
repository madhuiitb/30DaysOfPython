
language = "python"
lan_list = list(language)
print(lan_list)
print(type(lan_list))
print(len(lan_list))

print('-----------------------------------------------------')

lst = [i for i in language]
print(lst)
print(type(lst))
print(len(lst))
print('-----------------------------------------------------')

nums_list = [i for i in range(11)]
print(nums_list)
print(type(nums_list))
print(len(nums_list))
print('-----------------------------------------------------')

square_tuple = [(i, i**2) for i in range(5)]
print(square_tuple)
print(type(square_tuple[0]))
print(type(square_tuple))
print(len(square_tuple))
print('-----------------------------------------------------')

even_nums = [i for i in range(11) if i%2==0]
print(even_nums)
print(len(even_nums))
print(type(even_nums))
print('-----------------------------------------------------')

odd_numbers = [i for i in range(11) if i%2==1]
print(odd_numbers)
print(type(odd_numbers))
print(len(odd_numbers))
print('-----------------------------------------------------')

numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_nums = [i for i in numbers if i%2==0 and i>0]
print(positive_even_nums)
print(len(positive_even_nums))
print(type(positive_even_nums))
print('-----------------------------------------------------')

negative_odd_nums = [i for i in numbers if i%2==1 and i<0]
print(negative_odd_nums)
print(len(negative_odd_nums))
print(type(negative_odd_nums))

print('-----------------------------------------------------')

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flatten_lists = [number for row in list_of_lists for number in row]
print(flatten_lists)