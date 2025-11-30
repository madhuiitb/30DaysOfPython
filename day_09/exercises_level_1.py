age = input("Enter your age: ")
if int(age)>=18:
    print("You are old enough to learn to drive.")
else:
    print("You need {} years to learn to drive.".format(18-int(age)))


my_age = input("Enter my age: ")
your_age = input("Enter your age: ")

if my_age<your_age:
    print("You are older than my age.")
    if int(your_age)-int(my_age)==1:
        print("You are 1 year older than my age.")
    else:
        print("you are {} years older than my age".format(int(your_age)-int(my_age)))
elif my_age==your_age:
    print("We both are born at the same year")
else:
    print("My age is more")

