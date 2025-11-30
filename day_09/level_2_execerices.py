eighty = 80
hundred = 100
seventy = 70
sixty = 60
fifty = 50
marks_str = input("Enter your marks: ")
marks = int(marks_str)

if marks>=eighty:
    print("Your grade is A: ")
elif marks>=seventy and marks<eighty:
    print("Your grade is B: ")
elif marks>=sixty and marks<seventy:
    print("Your grade is C: ")
elif marks>=fifty and marks<sixty:
    print("Your grade is D: ")
else:
    print("Your grade is F: ")


autumn = ('september','october','november')
winter= ('december','january','february')
spring= ('march','april','june')
summer= ('july','august')

season = input("Enter your season : ")

if season=='september' or season=='october' or season=='november':
    print("Automn searson")
elif season=='january' or season=='february' or season=='december':
    print("Winter searson")
elif season=='march' or season=='april' or season=='june':
    print("Spring searson")
else:
    print("Summer searson")