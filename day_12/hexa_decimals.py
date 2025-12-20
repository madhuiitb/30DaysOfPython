import string
import random

def list_of_hexa_colors(length=3):
    hexa_colors = []
    hexa_chars = string.ascii_letters[:6] + string.digits
    for i in range(length):
        color = '#'
        for j in range(6):
            color += random.choice(hexa_chars)
        hexa_colors.append(color)
    return hexa_colors

hexa_colors_list = list_of_hexa_colors()
print("List of 3 random hexadecimal colors: ", hexa_colors_list)
print('-----------------------------------------------------')

def generate_rgb_color(length=3):
    rgb_list = []
    for _ in range(length):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        rgb_list.append((r, g, b))
    return rgb_list
rgb_color = generate_rgb_color()

print("Random RGB color: ", rgb_color)
print('-----------------------------------------------------')


def generate_colors(color_type, length=3):
    if  color_type.lower() == 'hexa':
        return list_of_hexa_colors(length)
    elif color_type.lower() == 'rgb':
        return generate_rgb_color(length)
    else:
        return "Invalid color type. Please choose 'hexa' or 'rgb'."
colors = generate_colors('hexa', 5)
print("Generating 5 colors of specified type (hexa): ", colors)
colors_rgb = generate_colors('rgb', 5)
print("Generating 5 colors of specified type (rgb): ", colors_rgb)

print(generate_colors('hexa', 3)) # ['#a3e12f','#03ed55','#eb3d2b'] 
print(generate_colors('hexa', 1)) # ['#b334ef']
print(generate_colors('rgb', 3))  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
print(generate_colors('rgb', 4))  # ['rgb(33,79, 176)']
print(generate_colors('rgb', 1))  # ['rgb(33,79, 176)']
print('-----------------------------------------------------')  


def random_seven_nums():
    seven_nums = set()
    while len(seven_nums) < 7:
        seven_nums.add(random.randint(0,9))
    return list(seven_nums)

seven_random_numbers = random_seven_nums()
print("Seven random numbers: ", seven_random_numbers)
print('-----------------------------------------------------')

def shuffle_list(input_list):
    shuffled_list = input_list[:]
    random.shuffle(shuffled_list)
    return shuffled_list
original_list = [1, 2, 3, 4, 5]
shuffled = shuffle_list(original_list)
print("Original list: ", original_list)
print("Shuffled list: ", shuffled)
print('-----------------------------------------------------')