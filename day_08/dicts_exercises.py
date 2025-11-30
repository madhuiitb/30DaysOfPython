print("------------------------------------------------")
print("Exercises for Dictionaries")
print("------------------------------------------------")
dog = {}
print(dog)

print("-----------------------------------------")
print("Adding properties for DOG dictionary")
print("-----------------------------------------")
dog['name']= 'Tom'
dog['color']="brown"
dog['breed']= 'German'
dog['legs']='straight'
dog['age']=2

print(dog)

print("-----------------------------------------")
print("Creating student dictionary")
print("-----------------------------------------")

student = {
    'first_name':'Vicky',
    'last_name':'Madhu',
    'gender':'male',
    'age':222,
    'is_married':False,
    'skills':['JavaScript','Python','React'],
    'country':"India",
    'address':{
        'city':'Hyd',
        'zip':500500
    }
}

print(student)
print("4. Length of student: ",len(student))

student_skills = student['skills']
print("5. Skills and type", student_skills, type(student_skills))

student['skills'].append('HTML')
student['skills'].append('CSS')

print("6. Modified student skills: ", student['skills'])




print("7. Keys : ", student.keys())
print("8. Values : ", student.values())
print("9. changing to list: ", list(student.items()))
del student['is_married']
print("10. del one item in student: ", student)

