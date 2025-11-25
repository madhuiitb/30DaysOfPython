print("------------------------------------------------")
# capitalize() : converts first char as CAPS of a string
print("capitalize() : method")
print("------------------------------------------------")
challenge = 'thirty days of python'
print(challenge.capitalize())


print("------------------------------------------------")
# count() : count(substring, start=.., end=..,)
# returns occurrences of substring
print("count() : method")
print("------------------------------------------------")
print(challenge.count('y'))
print(challenge.count('y', 7,14))
print(challenge.count('th'))

print("------------------------------------------------")
# endswith() : checks if a string ends with
print("endswith() : method")
print("------------------------------------------------")
print(challenge.endswith('on'))
print(challenge.endswith('python'))
print(challenge.endswith('tion'))

print("------------------------------------------------")
# expandtabs() : replaces tab character with spaces, default is 8,
# It takes tab size arguments
print("expandtabs() : method")
print("------------------------------------------------")
challenge_one='thirty\tdays\tof\tpython'
print(challenge_one.expandtabs())
print(challenge_one.expandtabs(12))

print("------------------------------------------------")
# find() : returns the index of first occurrence of substring, if not returns -1
print("find() : method")
print("------------------------------------------------")
print(challenge.find('y'))
print(challenge.find('th'))
print(challenge.find('on'))
print(challenge.find('tion'))

print("------------------------------------------------")
# rfind() : returns the index of last occurrence of substring, if not returns -1
print("rfind() : method")
print("------------------------------------------------")
print(challenge.rfind('y'))
print(challenge.rfind('th'))
print(challenge.rfind('on'))

print("------------------------------------------------")
# format() : formats string into a nicer out
print("format() : method")
print("------------------------------------------------")

f_name = 'Vicky'
l_name = 'Madhu'
age = 200
job = 'Student'
country = "India"
sentence = 'I am {} {}. I am {} years old. I live in {}.'.format(f_name, l_name, age, country)
print(sentence)


print("------------------------------------------------")
# index() : returns the lowest index of a substring
# index( default 0, length-1),
# not found valueError
print("index() : method")
print("------------------------------------------------")

sub_str = 'da'
print(challenge.index(sub_str))
#print(challenge.index(sub_str,9)) #valueError
print(challenge.index(sub_str,5))
print(challenge.index(sub_str,1))
print(challenge.index(sub_str,2))


print("------------------------------------------------")
# rindex() : returns the highest index of a substring
# rindex( default 0, length-1),
# not found valueError
print("rindex() : method")
print("------------------------------------------------")
print(challenge.rindex(sub_str))
# print(challenge.rindex(sub_str,9)) #valueError
print(challenge.rindex('on',8))


print("------------------------------------------------")
# isalnum() : checks alphanumeric character
print("isalnum() : method")
print("------------------------------------------------")
print(challenge.isalnum())

challenge_one = '30DaysPython'
print(challenge_one.isalnum())

challenge_two = "thirty days of python 2019"
print(challenge_two.isalnum())

challenge_three = "ThirtyDaysPython"
print(challenge_three.isalnum())

print("------------------------------------------------")
# isalpha() : checks if all string elements are alphabet chars ( a-z and A-Z)
print("isalpha() : method")
print("------------------------------------------------")
print(challenge.isalpha()) # False
print(challenge_one.isalpha()) #False
print(challenge_two.isalpha()) # False
print(challenge_three.isalpha()) # True

print("------------------------------------------------")
# isdecimal() : checks if all characters in a string are decimal (0-9)
print("isdecimal() : method")
print("------------------------------------------------")
print(challenge.isdecimal()) # False
print(challenge_one.isdecimal()) # False

challenge_four = '1234'
print(challenge_four.isdecimal()) # True

challenge_five = '\u00B2'
print(challenge_five.isdecimal())  # False

challenge_six = '123 4'
print(challenge_six.isdecimal()) # False

print("------------------------------------------------")
# isdigit() : checks if all characters in a string are numbers
# 0-9 and some other unicode characters for numbers
print("isdigit() : method")
print("------------------------------------------------")
print(challenge.isdigit()) # False

challenge_seven = "30"
print(challenge_seven.isdigit()) # True

challenge_eight = "\u00B2"
print(challenge_eight.isdigit()) # True

print("------------------------------------------------")
# isnumeric() : checks if all characters in a string are numbers
# or number related (just like isdigit(), just accepts more symbols like 1/2
print("isnumeric() : method")
print("------------------------------------------------")
num='10'
print(num.isnumeric()) # True
num_one='\u00BD'
print(num_one.isnumeric()) # True
num_two='10.2'
print(num_two.isnumeric()) # False

print("------------------------------------------------")
# isidentifier() : checks for a valid identifier
# it checks if a string is a valid variable name
print("isidentifier() : method")
print("------------------------------------------------")
print(challenge.isidentifier()) # False
print(challenge_one.isidentifier()) # False
print(challenge_two.isidentifier()) # False
print(challenge_three.isidentifier()) # True
print(challenge_four.isidentifier()) # False

print("------------------------------------------------")
# islower() : checks if all alphabet characters in the string are lowercase
print("islower() : method")
print("------------------------------------------------")
print(challenge.islower()) # True
print(challenge_one.islower()) # False
print(challenge_two.islower()) # True


print("------------------------------------------------")
# isupper() : checks if all alphabet characters in the string are uppercase
print("isupper() : method")
print("------------------------------------------------")
print(challenge.isupper()) # False

challenge_ten = 'TEN WAYS'
print(challenge_ten.isupper()) # True

print("------------------------------------------------")
# join() : returns a concatenated string
print("join() : method")
print("------------------------------------------------")

web_tech = ['HTML','CSS','JavaScript','React']
result = ' '.join(web_tech)
print(result)

result_concatenate = '#'.join(web_tech)
print(result_concatenate)

print("------------------------------------------------")
# strip() : removes all given characters starting from the beginning and end of the string
print("strip() : method")
print("------------------------------------------------")

print(challenge.strip('noth'))
print(challenge.strip('da'))

print("------------------------------------------------")
# replace() :  Replaces substring with a given string
print("replace() : method")
print("------------------------------------------------")

print(challenge.replace('python','JavaScript'))
print(challenge.replace('python','React'))

print("------------------------------------------------")
# split() :  Splits the string, using given string or space as a separator
print("split() : method")
print("------------------------------------------------")
print(challenge.split())
print(challenge.split(','))
challenge_11 = 'thirty, days, of, python'
print(challenge_11.split(','))

print("------------------------------------------------")
# title() : Returns a title cased string
print("title() : method")
print("------------------------------------------------")
print(challenge.title())
print(challenge_11.title())
print(challenge_one.title())
print(challenge_two.title())
print(challenge_three.title())

print("------------------------------------------------")
# swapcase() : Converts all uppercase chars to lowercase and all lowercase chars to uppercase chars
print("swapcase() : method")
print("------------------------------------------------")
print(challenge.swapcase())
print(challenge_one.swapcase())
print(challenge_two.swapcase())
print(challenge_three.swapcase())
print(challenge_11.swapcase())
print(challenge_one.swapcase())

print("------------------------------------------------")
# startswith() : Checks if string starts with the specified string
print("startswith() : method")
print("------------------------------------------------")
print(challenge.startswith('python'))
print(challenge_one.startswith('30'))
print(challenge_two.startswith('days'))
print(challenge.startswith('thirty'))