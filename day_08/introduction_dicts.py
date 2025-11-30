# A dictionary is a collection of unordered,
# Modifiable (mutable) paired  (Key: Value) data type

print("------------------------------------------------------")
print("Creating a dictionary ")
print("------------------------------------------------------")
empty_dict = {}
print(empty_dict)

dct = {"key1":"value1", "key2":"value2", "key3":"value3","key4":"value4"}
print(dct)

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

print("------------------------------------------------------")
print("Length of a dictionary ")
print("------------------------------------------------------")
print("Length of dict: ", len(dct))
print("Length of person dictionary: ", len(person))