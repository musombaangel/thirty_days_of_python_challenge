# Getting the first, middle and last item of a list
emp=[]
l=[3,2,4.2,3,2,5]
print(len(l))
middle=int((len(l)-1)/2)
print("First item: {}, middle item: {}, last item: {}".format(l[0], l[middle], l[-1]))

#list with many data types
mixed_data_types=["Angel",21,1.67,"Single","Nairobi"]
it_companies=["Facebook", "Google", "Microsoft", "Apple", "IBM"
              , "Oracle", "Amazon"]
print(mixed_data_types)
print("Number of companies: ",len(it_companies))

middle=int((len(it_companies)-1)/2)
print("First company: {}, middle company: {}, last company: {}".format(it_companies[0], it_companies[middle], it_companies[-1]))

#indexing with negative numbers
it_companies[-1]="Oracle"
print(it_companies)

#adding and inserting items
it_companies.append("Azure")
it_companies.insert(middle,"Meta")
it_companies[3]=it_companies[3].upper()
print(it_companies)

#joining the companies
joined='#;  '.join(it_companies)
print(joined)

#checking if a company is in the list
has_ms="Microsoft" in it_companies
print("Is microsoft in the list? ", has_ms)

#sorting
s=sorted(it_companies)
print(s)

#reversing the list
s_reverse=reversed(s)
print(list(s_reverse))

middle=int((len(it_companies)-1)/2)
print(middle)

first_3=s[:2]
last_3=s[-3:]
middle_comp=s[middle]
print("First three companies: {}. Last 3 companies: {}. Middle company: {}"
      .format(first_3, last_3, middle_comp))

print("Initial list: ", it_companies)
del it_companies[0]
print("No first value: ", it_companies)

import math
middle=len(it_companies)/2
top, bottom=math.ceil(middle), int(middle)

# Finding the middle value
if top==bottom:
    middle_val=it_companies[int(middle)]
else:
    middle_val=it_companies[bottom:top]/2
print("Middle value: ", middle_val)

it_companies.remove(middle_val)
print("No middle value: ",it_companies)

#deleting the last value
del it_companies[-1]
print("No last value: ",it_companies)

cleared=it_companies.clear()
print(cleared)

# Deleting the entire list
del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

#joining the two lists
joined=front_end+back_end
print(joined)

#copying the joined list
full_stack=joined.copy()
new1, new2="Python", "SQL"
full_stack.insert(5,new2)
full_stack.insert(5,new1)
print(full_stack)




#sorting and manipulating ages
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
s=sorted(ages)
print(s)

ages.append(min(ages))
ages.append(max(ages))
print(ages)

#finding the median, mean and range
middle=len(ages)/2
top, bottom=math.ceil(middle), int(middle)
if top==bottom:
    median=ages[int(middle)]
else:
    median=ages[bottom:top]

print("Median age: ", median)

average_age=sum(ages)/len(ages)
print("Mean age: ", average_age)

age_range=max(ages)-min(ages)
print("Range: ", age_range)

d1=abs(min(ages)-average_age)
d2=abs(max(ages)-average_age)
less_d1=d1<d2
if less_d1:
    print("The difference between the minimum and average is smaller")
else:
    print("The difference between the maximum and average is smaller")


#PART 3
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

#Middle countries
middle=(len(countries)-1)/2
bottom, top=int(middle), math.ceil(middle)
if bottom==top:
    middle_countries=countries[top]
else:
    middle_countries=countries[bottom:top]

print(middle_countries)


china, russia, usa, *scandic_countries=['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print(scandic_countries)