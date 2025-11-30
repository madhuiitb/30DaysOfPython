print("------------------------------------------------------")
print("Accessing items of a dictionary ")
print("------------------------------------------------------")
person = {
    "first_name": "Vicky",
    "last_name": "Madhu",
    "age":220,
    "country":"India",
    "is_married":False,
    "skills":['JavaScript','Python','React','Node','MongoDB'],
    'address':{
        'city': 'Hyderabad',
        'zipcode': '9410',
        'street': 'KPHB'
    }
}

f_name = person['first_name']
l_name = person['last_name']
print(f_name,l_name)

skills_js = person['skills'][0]
print(skills_js)

adds_city=person['address']['city']
print(adds_city)

print("------------------------------------------------------")
print("Accessing items of a dictionary using get():method ")
print("------------------------------------------------------")

print("First Name: ", person.get('first_name'))
print("Last Name: ", person.get('last_name'))

print("Skills: ", person.get('skills'))
print("Address: ", person.get('address'))
print("City: ", person.get('city'))

print("------------------------------------------------------")
print("Adding items to a dictionary ")
print("------------------------------------------------------")

person['phone'] = 987654321
print(person)
person['job_title']="Student"
print(person)
person['skills'].append("HTML")
print(person)

print("------------------------------------------------------")
print("Modifying items in a dictionary ")
print("------------------------------------------------------")
person['age']=230
print(person)

print("------------------------------------------------------")
print("Checking Keys in a dictionary ")
print("------------------------------------------------------")

print('first_name is in person? ', 'first_name' in person)
print('last_name is in person? ', 'last_name' in person)
print('city is in person? ', 'city' in person) #False

print("------------------------------------------------------")
print("Removing Key and value pairs from a dictionary ")
print("# pop(): removes item with key")
print("# popitem(): removes last item")
print("# del: removes an item with key")
print("------------------------------------------------------")

f_name_pop = person.pop("first_name")
print("first_name: pop(): ", f_name_pop)
last_item_pop=person.popitem()
print("removes last item: ", last_item_pop)
del person['is_married']
print("after del is_married: ", person)

print("------------------------------------------------------")
print("Changing dictionary to list ")
print("------------------------------------------------------")

person_list = list(person) # only keys
print(person_list)
person_items = list(person.items())
print(person_items)
print("------------------------------------------------------")
print(" Copy a Dictionary ")
print("------------------------------------------------------")
copy_person = person.copy()
print(copy_person)


print("------------------------------------------------------")
print(" Dictionary Keys ")
print("------------------------------------------------------")
keys = person.keys()
print(keys)

print("------------------------------------------------------")
print("Dictionary values")
print("------------------------------------------------------")
values = person.values()
print(values)
print("------------------------------------------------------")
print("Clearning a  dictionary ")
print("------------------------------------------------------")

person.clear()
print(person)