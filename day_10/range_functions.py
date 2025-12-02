print("---------------------------------------------")
print("The Range functions")
print("---------------------------------------------")
lst = list(range(11))
print(lst)

st = set(range(1,11))
print(st)
print("---------------------------------------------")
lst_even = list(range(0,11,2))
print(lst_even)

st_even = set(range(1,11,2))
print(st_even)
print("---------------------------------------------")
for num in range(11):
    print(num)

print("---------------------------------------------")
print("Nested for Loop")
print("---------------------------------------------")

person = {
    'first_name': 'Vicky',
    'last_name': 'Madhu',
    'age': 212,
    'country': 'India',
    'skills':['JavaScript','React','Python','Node'],
    'address': {
        'city': 'Hyderabad',
        'street':'VJY',
        'zipcode': '500500',
    }
}

for key in person:
    if key == 'skills':
        for skill in person[key]:
            print(skill)

print("---------------------------------------------")
print("For Else")
print("---------------------------------------------")

for num in range(11):
    print(num)
else:
    print("For loop ends: ",num)

print("---------------------------------------------")
print("Pass")
print("---------------------------------------------")

for num in range(6):
    pass