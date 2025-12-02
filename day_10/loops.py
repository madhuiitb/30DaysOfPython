print("---------------------------------------------")
print("Loops: ")
print("---------------------------------------------")
# Syntax
# while condition :
# code goes here

count = 0
while count < 10:
    print(count)
    count = count + 1
else :
    print("Final Count: ",count)


print("---------------------------------------------")
print("While Loops: Break and Continue ")
print("---------------------------------------------")
# Syntax
# while condition:
#   code goes here
#   if another_condition:
#       break

count_break = 0
while count_break < 5:
    print(count_break)
    count_break = count_break + 1
    if count_break == 3:
        break
print("Break Count: ",count_break)

print("---------------------------------------------")
print("While Loops: Break and Continue ")
print("---------------------------------------------")

test_count = 0
while test_count < 5:
    if test_count == 3:
        test_count = test_count + 1
        continue # Skips 3, or any other condition
    print(test_count)
    test_count = test_count + 1
print("Continue Count: ",test_count)