print("-------------------------------------------------")
print("Conditionals if/else ")
print("-------------------------------------------------")
# Sequential execution of the code / statements
# Top to bottom

a=3
if a>0 :
    print("A is a positive number")

if a<0 :
    print("A is a negative number")
else :
    print("A is an positive integer")

b=0
if b>0:
    print("B is a positive integer")
elif b<0:
    print("B is a negative integer")
else:
    print("B is zero")

print("-------------------------------------------------")
print("Short Hande if/else ")
print(" code if condition else code")
print("-------------------------------------------------")
# syntax
# code if condition else code

print("A is positive") if a>0 else print("A is negative")
print("B is positive") if b>0 else print("B is zero or negative")

print("-------------------------------------------------")
print(" Nested conditional if/else ")
print("-------------------------------------------------")

if a>4:
    if b>0:
        print("A is a positive integer")
    else:
        print("B is zero or negative")
else:
    print("A is positive or negative")

print("-------------------------------------------------")
print(" Condition and Logical operators ")
print("-------------------------------------------------")

c=0
if a>0 and a%2==0:
    print("A is an even and positive integer")
elif a>0 and a%2!=0:
    print("A is positive integer")
elif a==0:
    print("A is zero")
else:
    print("A is negative")


user = "editor"
access_level =2
if user=='admin' or access_level>=4:
    print("Access granted")
else:
    print("Access denied")
