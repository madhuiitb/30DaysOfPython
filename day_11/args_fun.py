print("-------------------------------------------------------")
print("Arbitrary Number of arguments")
print("-------------------------------------------------------")

def sum_all_nums(*nums):
    total=0
    for num in nums:
        total+=num
    return total
print(sum_all_nums(1,2,3,4,5))


print("-------------------------------------------------------")
print("Arbitrary Number of arguments of parameters in functions")
print("-------------------------------------------------------")

def generate_groups(team, *args):
    print(team)
    for i in args:
        print(i)
print(generate_groups('team-1','Vicky','Madhu','Dad'))

print("-------------------------------------------------------")
print("Function as a parameter of another function")
print("-------------------------------------------------------")

def square_num(num):
    return num**2

def do_something(fun, x):
    return fun(x)

print(do_something(square_num, 3))