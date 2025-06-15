empty=()
print(type(empty))  #tuple

sisters=("Jabari", "Kui")
brothers=("Musa", "Muriuki")

# Concatenating tuples
siblings=sisters+brothers
print(siblings)

#concatenating tuples with a single item which is in tuple format
family_members=siblings+("Marilyn",)+("Joe",)
print(family_members)

#slicing tuples
sibs=family_members[:3]
parents=family_members[-2:]
print(sibs)
print(parents)

fruits=("Apple","Lime","Kiwi")
veges=("Spinach","Cabbage")
animal_prods=("Milk", "Eggs", "Meat")

food_stuff_tp=fruits+veges+animal_prods
#converting to list
food_stuff_lt=list(food_stuff_tp)

import math
# Finding the middle item
middle=len(food_stuff_lt)//2
if int(middle)== math.ceil(middle):
    mid_item=food_stuff_lt[int(middle)]
else:
    mid_item=food_stuff_lt[int(middle):math.ceil(middle)]

print(mid_item)
first_three=food_stuff_lt[:3]
print(first_three)
last_three=food_stuff_lt[-3:]
print(last_three)

#deleting the tuple
del food_stuff_tp

#checking if an item is in a tuple
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)