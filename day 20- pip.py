import requests
import json

#Read this url
url='http://www.gutenberg.org/files/1112/1112.txt'  #url not available anymore
response=requests.get(url)
print(response) #404, site not available

# find max and min weight and years
url='https://api.thecatapi.com/v1/breeds'   #url with info on cats
response=requests.get(url)
print(response.headers)
cats_json=response.json()
print(cats_json[0])
needed_data=[]  #list to store the necessary data (name, weight, lifespan)

import re
'''Function that takes a string e.g., "7-8" and calculates the average version for that record
Example input: '5-7'
Example output: 6
'''
def calculate_value(s):
    values=re.findall(r'\d+', s) #list of the minimum and maximum values of the range
    values=map(float, values)
    result=sum(values)/2    #find the average within that range
    return result

for item in cats_json:
    needed_data.append([item['name'], calculate_value(item['weight']['imperial']), calculate_value(item['weight']['metric']), calculate_value(item['life_span'])])
print(needed_data)


min_imperial_weight=min([item[1] for item in needed_data])
max_imperial_weight=max([item[1] for item in needed_data])

min_metric_weight=min([item[2] for item in needed_data])
max_metric_weight=max([item[2] for item in needed_data])

min_age=min([item[3] for item in needed_data])
max_age=max([item[3] for item in needed_data])

for item in needed_data:
    #For imperial weight (index 1)
    if item[1] == min_imperial_weight:
        print("Minimum imperial weight:", item[0], "with weight", item[1])
    if item[1] == max_imperial_weight:
        print("Maximum imperial weight:", item[0], "with weight", item[1])
    #For metric weight (index 2)
    if item[2] == min_metric_weight:
        print("Minimum metric weight:", item[0], "with weight", item[2])
    if item[2] == max_metric_weight:
        print("Maximum metric weight:", item[0], "with weight", item[2])    
    #For age (index 3)
    if item[3] == min_age:
        print("Minimum age:", item[0], "with age", item[3])
    if item[3] == max_age:
        print("Maximum age:", item[0], "with age", item[3])



from bs4 import BeautifulSoup
import requests

url='https://www.sciencefocus.com/the-human-body/the-disappearing-y-chromosome'
response=requests.get(url)
print(response)

soup=BeautifulSoup(response.text,'html')
print(soup.prettify())