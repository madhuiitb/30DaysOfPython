import random
import string
print("--------------------------------------")
print("Random user id generator")
print("--------------------------------------")
items = string.ascii_letters + string.digits
def random_user_id(length=6):
    id=''
    for i in range(length):
        id = id + random.choice(items)
    return id

print(random_user_id())

print("--------------------------------------")
print("Taking input from user for length of id and how many ids")
print("--------------------------------------")


def user_id_gen_by_user():
    id_length = int(input("Enter length of id: "))
    no_of_ids = int(input("Enter number of ids to generate: "))
    for j in range(no_of_ids):
        print(random_user_id(id_length))

user_id_gen_by_user()
print('-----------------------------------------------------')

def rgb_color_gen():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return f"rgb({r},{g},{b})"

rgb_color = rgb_color_gen()
print("Random RGB color: ", rgb_color)

digits = string.digits
def random_0_255():
    while True:
        value = ''.join(random.choices(digits, k=3))
        if int(value) <= 255:
            return value

def rgb_color_gen_two_fun():

    r = random_0_255()
    g = random_0_255()
    b = random_0_255()
    return f"rgb({r},{g},{b})"
rgb_color_two = rgb_color_gen_two_fun()
print("Random RGB color using two functions: ", rgb_color_two)
print('-----------------------------------------------------')
