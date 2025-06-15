import re
#make a list with each of the words and the number of times it appears
paragraph = '''I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'''
splitted_paragraph=re.findall(r'\w+', paragraph)
words=[]
counts=[]
for word in splitted_paragraph:
    if word not in words:
        words.append(word)
        counts.append(1)
    else:
        ind=words.index(word)
        counts[ind]+=1


word_count=list(zip(words, counts))
print(word_count)
maxi=max(word_count, key=lambda x:x[1])
print("Maximum: ", maxi)

#find the distance between the minimum and maximum points
points = ['-12', '-4', '-3', '-1', '0', '4', '8']
int_points=sorted([int(point) for point in points])
maxi=max(int_points)
mini=min(int_points)
distance=maxi-mini
print(int_points)
print(distance)

#build a function to check for valid variable names
def is_valid_variable(v_name):
    pattern_match=re.match(r'^[a-z][a-z|_]*$', v_name)
    if pattern_match:
        return True
    else:
        return False

print(is_valid_variable('first_name'))
print(is_valid_variable('first-name'))
print(is_valid_variable('1first_name'))
print(is_valid_variable('firstname'))

#remove the unnecessary characters
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
clean=re.sub(r'[^\w\s\.]','', sentence)
print(clean)
