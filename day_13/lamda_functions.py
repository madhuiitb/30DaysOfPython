
print("-----------------------------------------")
x = lambda param1, param2, param3 : param1 + param2 + param3
print(x(1,2,3))

print("-----------------------------------------")
print("Named functions")
print("-----------------------------------------")
def add_two_nums(num1,num2):
    return num1 + num2
print(add_two_nums(2,3))

print("-----------------------------------------")
print("Anonymous functions")
print("-----------------------------------------")
(lambda a,b : a+b)(4,3)

print("-----------------------------------------")
square = lambda x:x**2
print(square(2))

cube = lambda x:x**3
print("Cube: ",cube(2))


multiple_operations = lambda a,b,c : a ** 2 - b * 1 + c
print("multiple_operations: ", multiple_operations(1,2,3)) 
print("multiple_operations: ", multiple_operations(2,2,3)) 

print("-----------------------------------------")
print("Lamda functions inside another functions")
print("-----------------------------------------")

def pow_function(n):
    return lambda x:x**n
print(pow_function(2)(4))

print("-----------------------------------------")
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]

even_nums  = lambda numbers: list(filter(lambda i: i%2==0 and i>0,numbers))
print(even_nums(numbers))

negative_odd_nums = lambda numbers: list(map(lambda i: i<0 and i**2, numbers))
print(negative_odd_nums(numbers))


print("-----------------------------------------")
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

flatten_lists = [ num for row in list_of_lists for col in row for num in col]

print("Flatten list: ", flatten_lists)


#[(0, 1, 0, 0, 0, 0, 0),
#(1, 1, 1, 1, 1, 1, 1),
#(2, 1, 2, 4, 8, 16, 32),
#(3, 1, 3, 9, 27, 81, 243),
#(4, 1, 4, 16, 64, 256, 1024),
#(5, 1, 5, 25, 125, 625, 3125),
#(6, 1, 6, 36, 216, 1296, 7776),
#(7, 1, 7, 49, 343, 2401, 16807),
#(8, 1, 8, 64, 512, 4096, 32768),
#(9, 1, 9, 81, 729, 6561, 59049),
#(10, 1, 10, 100, 1000, 10000, 100000)]

list_tuples = [(i,1,i,i**2,i**3,i**4,i**5) for i in range(11)]
for tup in list_tuples:
    print(tup)

print("-----------------------------------------")
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
#output:
#[['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]

contry_cap = [[i.upper(),i[:3].upper(),j.upper()] for row in countries for i,j in row]

print("Country Cap list: ", contry_cap)

print("---------------------------------------------------")
#output:
#[{'country': 'FINLAND', 'city': 'HELSINKI'},
#{'country': 'SWEDEN', 'city': 'STOCKHOLM'},
#{'country': 'NORWAY', 'city': 'OSLO'}]

contries_dict = [ {'country':country.upper(), 'city':city.upper()}for row in countries for country, city in row]
print("Country dict list: ", contries_dict)

print("---------------------------------------------------")
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
#output
#['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']

full_names = [ i+" "+j for row in names for i,j in row ]
print("full names: ", full_names)



print("---------------------------------------------------")

#y=mx+c

def slope(m,c):
    return lambda x: m*x+c

print("Slope: ", slope(2,3)(2))
