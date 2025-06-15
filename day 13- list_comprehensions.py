numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
pos=[num for num in numbers if num>=0]
#print(pos)


list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
l1=[l[0] for l in list_of_lists]
l2=[val for val in l1[0]]+[val for val in l1[1]]+[val for val in l1[2]]
#print(l2)

tuple_vals=[]
for i in range(0,11):
    initial=[i]
    others=[i**j for j in range(6)]
    record=initial+others
    tuple_vals.append(tuple(record))

#print(tuple_vals)


countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
c1=[c[0] for c in countries]
#print(c1)
c2=[list(country for country in c1[0])]+[list(country for country in c1[1])]+[list(country for country in c1[2])]
#print(c2)


names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
ind_names=[" ".join(name[0]) for name in names]
#print(ind_names)

sloper=lambda x1, x2, y1, y2:(abs(y1-y2))/(abs(x1-x2))
#print(sloper(1,4,2,3))