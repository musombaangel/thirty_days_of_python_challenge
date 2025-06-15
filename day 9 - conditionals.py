age=float(input("Enter your age: "))
d=18-age

#if... else statements

if age>18:
    print("You are old enough to drive")
else:
    print("you need {} more years to be able to drive".format(int(d)))

my_age=22
your_age=float(input("Enter your age: "))
d=abs(your_age-my_age)

if my_age>your_age:
    print("I am {} years older than you".format(int(d)))
else:
    print("You are {} years older than me".format(int(d)))

a=int(input("Enter number one: "))
b=int(input("Enter number two: "))

if a>b:
    print("a is greater than b")
elif a<b:
    print("b is greater than a")
else:
    print("a and b are equal")


score=float(input("Enter score: "))

#if... elif... else statements
if score>=90:
    print("A")
elif score>=70:
    print("B")
elif score>=60:
    print("C")
elif score>=50:
    print("D")
else:
    print("F")


month=input("Enter the month: ")
if month=="September" or month=="November" or month == "October":
    sn="Autumn"
elif month == "March" or month == "April" or month == "May":
    sn = "Spring"
elif month == "June" or month == "June" or month == "July":
    sn = "Summer"
elif month == "December" or month == "January" or month == "February":
    sn = "Winter"
else:
    sn="Invalid. Not a real month or if it is, start with a capital letter. "

print("The season is {}".format(sn))

fruit=input("Enter fruit: ")
fruits = ['banana', 'orange', 'mango', 'lemon']

fruits.append(fruit) if fruit not in fruits else print("{} is already in the list".format(fruit))
print(fruits)

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

if 'skills' in person.keys():
    mid=int((len(person['skills'])-1)/2)
    print("middle skill: ", person['skills'][mid])

    if 'Python' in person['skills']:
        print("Person has python skills.")
    
    if ('JavaScript' and "React") in person['skills'] and ('Node' or 'Python' or 'MongoDB') not in person["skills"]:
        print("He is a front-end developer.")
    elif ('JavaScript' or "React") not in person['skills'] and ('Node' or 'Python' or 'MongoDB') in person["skills"]:
        print('He is a backend developer')
    elif('React' and 'Node' and "MongoDB") in person['skills']:
        print('He is a fullstack developer')
    else:
        print('unknown title')

first=person['first_name']
last=person['last_name']
country=person['country']
print(first)
print('{} {} lives in {}'.format(first, last, country))