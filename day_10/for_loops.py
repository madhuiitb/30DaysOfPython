print("---------------------------------------------")
print("For Loops: ")
print("---------------------------------------------")
numbers = [0,1,2,3,4,5]
for number in numbers:
    print(number)

print("---------------------------------------------")
language = 'python'
for letter in language:
    print(letter)

print("---------------------------------------------")
for i in range(len(language)):
    print(i,language[i])


print("---------------------------------------------")
nums = (0, 1, 2, 3, 4, 5)
for num in nums:
    print(num)
print("---------------------------------------------")
for i in range(len(nums)):
    print(i,nums[i])
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
    print(key,person[key])
print("---------------------------------------------")

for key, value in person.items():
    print(key,value)
print("---------------------------------------------")

it_companies = {'meta','amazon','microsoft','netflix'}
for company in it_companies:
    print(company)

print("---------------------------------------------")
print("For Loops: Break and Continue ")
print("---------------------------------------------")

for num in nums:
    print(num)
    if num==3:
        break

print("---------------------------------------------")
for num in nums:
    print(num)
    if num==3:
        continue
    print('next num should be ', num+1) if num!=5 else print("Loop ends")

print("---------------------------------------------")
