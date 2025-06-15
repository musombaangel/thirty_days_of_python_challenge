#concatenation
s='Thirty '+ ' Days '+ ' Of '+ ' Python.'
print(s)

s2='Coding '+ ' For ' + ' All.'
print(s2)

company=s2
print(company)
print(len(company))

#upper and lower methods
print("uppercase: ",company.upper())
print("lowercase: ",company.lower())

#slicing
first_word=company[:6]
print(first_word)

#returning the index where a string is found
print(company.rfind("Coding"))
print(company)
print(company.index("Coding"))

#replace
print(s2.replace("Coding", "Python"))

s3="Python for Everyone"
print(s3.replace("Everyone","All"))

#split method
s4='Coding For All'
print(s4.split())

s5="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(s5.split(","))

print(company[0])
print(company[-1])

#abbreviations
s='Python For Everyone'
s=[letter for letter in s if letter.isupper()]
print("".join(s))

s='Coding For All'
s_list=[letter for letter in s if letter.isupper()]
print("".join(s_list))


#finding first index
print(s.index("C"))
print(s.index("F"))

#finding last index
s="Coding For All People."
print(s.rfind("l"))
print(s.rindex("l"))

s= 'You cannot end a sentence with because because because is a conjunction'
s.find("because")
s.rindex("because")

print(s.replace(" because because because",""))

#startswith and endswith
print(company.startswith("Coding"))
print(company.endswith("coding"))

#strip method
tabbed='   Coding For All      ' 
print(tabbed.strip(" "))

#check if valid variable names
s1, s2="30DaysOfPython","thirty_days_of_python"
print(s1.isidentifier())
print(s2.isidentifier())

#join strings in a list
l=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print("# ".join(l))

#skipping a line
s="I am enjoying this challenge.\nI just wonder what is next."
print(s)

#tab
s="Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki"
print(s)

#format
radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius {} is {} meters square.".format(radius,area))

#multiline f string
print(f'''8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144''')
