# creating a set
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


print(len(it_companies))

#adding items
it_companies.add("Twitter")
print(it_companies)

#updating items
new = ('Tesla','OpenAI','Meta')
it_companies.update(new)
print(it_companies)
#updated=A.update(B)

#removing items
it_companies.remove('Tesla')
print(it_companies)

it_companies.discard('Apple')    # no difference
print(it_companies)


#set operations
inter=A.intersection(B)
is_sub=A.issubset(B)
is_dis=A.isdisjoint(B)
aub=A.union(B)
bua=B.union(A)
diff=A.symmetric_difference(B)
#print("joined: ", updated)
print("intersection: ", inter)
print("is subset: ", is_sub)
print("is disjoint: ", is_dis)
print("union A,B: ", aub)
print("union B,A: ", bua)
print("symmetric difference: ", diff)
print("difference A-B: ", A-B)
del A
del B
#print(A)    #returns an error since A has been deleted

#length of a set
age_l = [22, 19, 24, 25, 26, 24, 25, 24]
age_s = set(age)
print(len(age_l))
print(len(age_s))

#making a set from a string
sent = "I am a teacher and I love to inspire and teach people".split()
print(sent)
sent = set(sent)
print(sent)

