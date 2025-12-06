print("-------------------------------------------------------")
print("Exercise: 1")
print("-------------------------------------------------------")

def add_two_numbers(num1, num2):
    return num1 + num2
print(add_two_numbers(4, 2))

print("-------------------------------------------------------")
print("Exercise: 2")
print("-------------------------------------------------------")

def area_of_circle(r):
    PI=3.14
    return PI*r**2
print(area_of_circle(5))

print("-------------------------------------------------------")
print("Exercise: 3")
print("-------------------------------------------------------")

def add_all_nums(*args):
    total=0
    for num in args:
        if type(num)!=int:
            print("This is {} not a number".format(num))
        else:
            total += num
    return total

print(add_all_nums(1,2,3,4,'5',6,7,'8',9,10))

print("-------------------------------------------------------")
print("Exercise: 4")
print("-------------------------------------------------------")

def convert_celsius_to_fahrenheit(temp_c):
    temp_fahrenheit=(temp_c*9/5)+32
    return temp_fahrenheit
print(convert_celsius_to_fahrenheit(14))

print("-------------------------------------------------------")
print("Exercise: 5")
print("-------------------------------------------------------")
autumn = ['aug','sep','oct','nov']
winter = ['dec','jan','feb']
spring = ['mar','apr']
summer = ['may','jun','jul']
def check_season(month):
    if month in winter:
        return "winter"
    elif month in spring:
        return "spring"
    elif month in summer:
        return "summer"
    else:
        return "autumn"
print(check_season('sep'))
print(check_season('jan'))

print("-------------------------------------------------------")
print("Exercise: 7")
print("-------------------------------------------------------")

def solve_quadratic_eqn(x, a=1,b=1,c=1):
    return a*x**2+b*x+c

print(solve_quadratic_eqn(2))



print("-------------------------------------------------------")
print("Exercise: 8")
print("-------------------------------------------------------")

def print_list(*args):
    for num in args:
        print(num)
print(print_list(1,2,3,4))


print("-------------------------------------------------------")
print("Exercise: 9")
print("-------------------------------------------------------")

def reverse_list(nums):
    reverse_nums=[]
    for num in nums:
        print(num)
        reverse_nums = [num]+reverse_nums
    print(reverse_nums+nums)
    return reverse_nums
print(reverse_list([1,2,3,4,5]))
print(reverse_list(["A","B","C","D","E"]))

print("-------------------------------------------------------")
print("Exercise: 11")
print("-------------------------------------------------------")
food_staff = ['Potato','Tomato','Mango','Milk']
def add_item(food_items, new_item):
    food_items.append(new_item)
    return food_items
print(add_item(food_staff,"Meat"))

numbers = [1,2,3,4,5]
print(add_item(numbers,6))

print("-------------------------------------------------------")
print("Exercise: 12")
print("-------------------------------------------------------")

def remove_item(food_items, new_item):
    food_items.remove(new_item)
    return food_items
print(remove_item(food_staff,"Tomato"))

print(remove_item(numbers,2))


print("-------------------------------------------------------")
print("Exercise: 13")
print("-------------------------------------------------------")

def sum_of_numbers(num):
    total=0
    for i in range(num+1):
        total=total+i
    return total
print(sum_of_numbers(5))
print(sum_of_numbers(10))
print(sum_of_numbers(100))

print("-------------------------------------------------------")
print("Exercise: 14")
print("-------------------------------------------------------")

def sum_of_odds(num):
    total=0
    for i in range(num+1):
        if i%2!=0:
            total=total+i
    return total
print(sum_of_odds(5))
print(sum_of_odds(10))
print("-------------------------------------------------------")
print("Exercise: 1")
print("-------------------------------------------------------")

print("-------------------------------------------------------")
print("Exercise: 1")
print("-------------------------------------------------------")