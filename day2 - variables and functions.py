# Day 2: 30 days of python programming
# VARIABLES
first_name="Holly"
last_name="Martin"
full_name=first_name+" "+last_name
country="Kazakhstan"
city="Almaty"
age=45
year=2025
Is_married=False
Is_true=False
is_light_on=True
#Assigning multiple variables in one line
book, author, Is_good="A little life", "Hanya Yanagihara", True

#TYPES
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(Is_married))
print(type(Is_true))    
print(type(is_light_on))
print(type(book))
print(type(author)) 

#LENGTH
print(len(first_name))
print(len(last_name))
print("Maximum length:",max(len(first_name), len(last_name)))

#COMPUTATION
num_one=5
num_two=4
total=num_one+num_two
diff=num_one-num_two
remainder=num_one%num_two
exp=num_one**num_two
floor_division=num_one//num_two

radius=30
pi=3.14
area_of_circle=pi*(radius**2)
circum_of_circle=2*pi*radius

#INPUT

r=int(input("Enter radius: "))
area=pi*(r**2)
print("Area of the circle:",area)

first_name, last_name, country, age = input("Enter first name, last name, country and age separated by a space: ").split()
print(first_name)

#HELP
help('keywords')

# CASTING
# int to float
num_int = 10
print('num_int',num_int)       
num_float = float(num_int)
print('num_float:', num_float)  

# float to int
gravity = 9.814
print(int(gravity))       

# int to str
num_int = 10
print(num_int)                 
num_str = str(num_int)
print(num_str)                 

# str to int or float
num_str = '10.9'
num_float = float(num_str)
print('num_float', float(num_str))  
num_int = int(num_float)
print('num_int', int(num_int))      

# str to list
first_name = 'Potato'
print(first_name)              
first_name_to_list = list(first_name)
print(first_name_to_list)       