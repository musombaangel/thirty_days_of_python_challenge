#Count the number of lines and words in Obama's speech
speeches=['txt_files/obama_speech', 'txt_files/michelle_speech.txt', 'txt_files/trump_speech.txt']
for speech in speeches: 
    with open(speech) as f:
        print('for ',speech)
        lines=0     #counter for lines
        words=0     #counter for words

        for line in f.read().splitlines():
            lines+=1
            line_words=line.split(" ")
            for word in line_words:
                if word:        #prevent empty lines from being counted as words
                    words+=1

    print("The total number of lines are ", lines)
    print("The total number of words are ", words)



import json
#Create a function that finds the ten most spoken languages
with open('json_files/country_data.json','r', encoding='utf-8') as f:
    j_countries=json.load(f)    #reading from the json
    langs={}    #list for storing the languages
    for item in j_countries:
        for key, value in item.items():
            if key=='languages':
                for v in value:
                    if v not in langs:
                        langs[v]=1
                    else:
                        langs[v]+=1

vals=langs.values()
sorted_vals=sorted(vals)
popular=[]

for i in range(10):
    for key, value in langs.items():
        if value==max(langs.values()):
            popular.append((key,value))
            langs[key]=-1
            if len(popular)>=10:
                break
        
popular=popular[:10]
print(popular)


#Build a function that finds the 10 most populated countries
import json
with open('json_files/country_data.json','r', encoding='utf-8') as f:
    j_countries=json.load(f)    #reading from the json
    print(j_countries)
    ordered=sorted(j_countries, key=lambda x:x['population'], reverse=True)
    top_10=ordered[:10]
    for country in top_10:
        print(country['name'], country['population'])   #10 most populated countries


import re
#extract email addresses from the email.txt file
with open ('txt_files/emails.txt') as f:
    emails=[]   #list to store email addresses
    for line in f.readlines():
        words=line.split(" ")
        pattern=r'^[a-z]+@[a-z]+.[a-z]*$'
        for word in words:
            if re.match(pattern, word):
                if '\n' in word:
                    word=re.sub('\n','',word)   #remove the end-line string from the email address
                    emails.append(word)     #add the email address to the list   
    emails=set(emails)  #select unique values
    print(emails)

#find the most common words
txt="I know that I have a lot of reading that I must do to be able to finish this course. The course is very hard but I will manage"
words=[]    #list to store words
count=[]
s_txt=txt.split(" ")
print(s_txt)
for word in s_txt:
    word=re.sub(r'[^a-z]', "", word)
    if word not in words:
        words.append(word)
        count.append(1)
    else:
        id=words.index(word)
        count[id]+=1
word_count=list(zip(words, count))
print(word_count)

import re
#write a function to find the most frequent words in the speeches
def most_common(txt, n):
    txt=txt.strip(' ')
    txt=re.sub(r'[^\w\s]', '', txt)   #remove punctuation marks
    s_txt=txt.split(" ")
    words=[]
    count=[]
    for word in s_txt:
        word=re.sub(r'[^a-z]', "", word)
        if not word:
            pass
        elif word not in words:
            words.append(word)
            count.append(1)
        else:
            id=words.index(word)
            count[id]+=1
    word_count=list(zip(words, count))
    final_word_count=sorted(word_count, key=lambda x:x[1], reverse=True)
    return final_word_count[:n]


speeches=['txt_files/obama_speech', 'txt_files/michelle_speech.txt', 'txt_files/trump_speech.txt']
for speech in speeches:
    print(speech)
    with open(speech) as f:
        info=""
        for line in f.readlines():
            info+=line
        print(most_common(info,10))

#how similar are the words in the speeches
import re
from sklearn.metrics.pairwise import cosine_similarity
#list of stop words provided
stop_words = ['i','me','my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up','down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
def clean_speech(txt):
    l_txt=txt.lower()   #lowercase
    c_txt=re.sub(r'[^\w\s]', '', l_txt)    #remove punctuation marks
    words=c_txt.split(" ")
    clean=""    #variable to store clean texts
    for word in words:
        if word not in stop_words:
            clean=clean+word+" "    #combining non-stop-words
    return clean

def similarity_finder(txt1, txt2):
    dictionary=[]   #var to store all words
    words_1=txt1.split(" ")
    words_2=txt2.split(" ")
    for word in words_1:
            dictionary.append(word)
    for word in words_2:
            dictionary.append(word)
    dictionary=set(dictionary)

    dict1={}    #var to store all the words in the first text and their count
    dict2={}    #var to store all the words in the second text and their count
    for word in words_1:
        if word not in dict1:
            dict1[word]=1
        else:
            dict1[word]+=1
    for word in words_2:
        if word not in dict2:
            dict2[word]=1
        else:
            dict2[word]+=1

    vec1=[]
    vec2=[]
    for word in dictionary: #create a vector for the count of each dictionary word in each text
        if word in dict1:
            vec1.append(dict1[word])
        else:
            vec1.append(0)
        if word in dict2:
            vec2.append(dict2[word])
        else:
            vec2.append(0) 
        
    return cosine_similarity([vec1], [vec2])[0][0]  #calculate similarity

#reading the files and combining the lines
with open("txt_files/melania_speech.txt") as m:
    melania=m.read().splitlines()
with open("txt_files/michelle_speech.txt") as mo:
    michelle=mo.read().splitlines()
mel=" ".join(melania)
mich=" ".join(michelle)

#cleaning the data
c_mel=clean_speech(mel)
c_mich=clean_speech(mich)

#similarity computation
print(similarity_finder(c_mel, c_mich))    


#find the 10 most repeated words in the romeo_and_juliet.txt
with open("txt_files/romeo_and_juliet.txt") as f:
    txt=f.read().splitlines()
    combined_txt=" ".join(txt)
    print(most_common(clean_speech(combined_txt),10))

import csv
import re
with open('csv_files/hacker_news.csv') as f:
    csv_reader = csv.reader(f, delimiter=',') # w use, reader method to read csv
    py=0
    js=0
    java=0
    for row in csv_reader:
        if re.search(r'[Pp]ython', row[2]):
            py+=1
        if re.search(r'[Jj]ava[Ss]cript', row[2]):
            js+=1
        if re.search(r'[Jj]ava', row[2]) and not re.search(r'[Jj]ava[Ss]cript', row[2]):
            java+=1
print("Number of rows with python:", py)
print("Number of rows with javascript:", js)
print("Number of rows with java:", java)