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
