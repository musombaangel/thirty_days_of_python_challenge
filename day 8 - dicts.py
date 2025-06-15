dog={}
dog['name']="Spot"
dog['color']="Black"
dog['breed']="Japanese Spitz"
dog["legs"]=4
dog["age"]=5
print(dog)

#Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name' : 'Angel',
    'last_name' : 'Romeo',
    'gender' : 'NB',
    'age' : 22,
    'marital_status' : 'taken',
    'skills' : 'r,python,java',
    'country' : 'Ugake',
    'city' : 'Naimpala',
    'address' : 'USIU'
}
print(len(student))

print('skills:', student['skills'])
print(type(student["skills"]))

student["skills"]="r, python, Java, tuba, pole dance, pottery"
print(student['skills'])

stud = student.keys()
print(stud)

val = student.values()
print(val)

student_items=student.items()
print(student_items)

del student["marital_status"]
print(student)

del student
#print(student)
