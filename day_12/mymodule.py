print('-------------------------------------------------------')
print("My module file")
print('-------------------------------------------------------')

def generate_full_name(first_name, last_name):
    space = ' '
    return first_name+ space + last_name


def sum_two_numbers(num_one, num_two):
    return num_one + num_two

def person(name, age,weight,height):
    person_dict={
        'person_name':name,
        'age':age,
        'weight':weight,
        'height':height,
        'mass':weight*height,
    }
    return person_dict

