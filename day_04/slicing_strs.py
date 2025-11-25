print("-------------------------------------------")
print("Accessing from right end, Negative index")
print("-------------------------------------------")
language = "Python"
last_letter = language[-1]
second_last = language[-2]

print(last_letter)
print(second_last)

print("--------------------------------------------")
print("Slicing python strings")
print("--------------------------------------------")

first_three = language[0:3]
last_three = language[3:6]
print(first_three)
print(last_three)
print("Another way")
last_three_another_way = language[-3:]
print(last_three_another_way)
print("One more way")
last_three_one_way = language[3:]
print(last_three_one_way)

print("--------------------------------------------")
print("Reversing a strings")
print("--------------------------------------------")

greeting = "Hello, World!"
print(greeting[::-1])
print("--------------------------------------------")


print("--------------------------------------------")
print("Skipping characters while slicing")
print("--------------------------------------------")
pto = language[0:6:2] # skipping 1 chars
ph = language[0:6:3] # skipping 2 chars
po = language[0:6:4] # skipping 3 chars
print(pto)
print(ph)
print(po)