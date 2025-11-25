a=6
b=4

print(f'{a}+{b}={a+b}')
print(f'{a}-{b}={a-b}')
print(f'{a}*{b}={a*b}')
print(f'{a}/{b}={a/b}')
print(f'{a}//{b}={a//b}')
print(f'{a}%{b}={a%b}')
print(f'{a}**{b}={a**b}')

print("-------------------------------------------")

# Python strings as  sequence of characters
print('Python strings as  sequence of characters')

print("-------------------------------------------")
language = "Python"
a,b,c,d,e,f = language # Unpacking sequence characters into variable
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print("-------------------------------------------")

print("Accessing characters in strings by index")
print("-------------------------------------------")

first_letter = language[0]
second_language = language[1]
last_index = len(language)-1
last_letter = language[last_index]

print(first_letter)
print(second_language)
print(last_letter)
print("-------------------------------------------")
