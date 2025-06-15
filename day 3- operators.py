#area of a triangle
age=22
height=1.66
comp= 4+8j
base=int(input("Enter base of the triangle: "))
height=int(input("Enter height of the triangle: "))
area=0.5*base*height
print("The area is ", area)

#perimeter
a=int(input("Enter side a: "))
b=int(input("Enter side b: "))
c=int(input("Enter side c: "))
perimeter=a+b+c
print("The perimeter is: ", perimeter)

#perimeter of a rectangle
length=int(input("Enter length: "))
width=int(input("Enter width: "))
r_perimeter=2*(length+width)

#y intercept
x=0
y_int = 2*x-2
print("Y intercept: ", y_int)

#x intercept
y=0
x_int=0.5*(y+2)
print("X intercept: ", x_int)

#finding the slope between two points
x1,y1=(0,y_int)
x2,y2=(x_int,0)
m1=y2-y1/x2-x1
print("Slope 1:", round(m1,2))

#slope 2
x1, y1=(2,2)
x2, y2=(6,10)
m2=y2-y1/x2-x1
print("Slope 2: ", round(m2,2))

#euclidean distance
euc_dist=((x2-x1)**2+(y2-y1)**2)**0.5
print("Euclidean distance: ", euc_dist)

#comparison of the two slopes
print("The smaller slope is ", min(m1,m2), " and the larger one is ", max(m1,m2))

#input x and calculate y
x=float(input("Enter x: "))
y=x**2 + 6*x + 9
print("Your y is ", y)

#compare length of python and dragon
len_1, len_2=len("python"), len("dragon")
is_equal=(len_1==len_2)
print("Equality of words: ", is_equal)

#check for on
has_on=("on" in "python") and ("on" in "dragon")
print("Both dragon and python have 'on'? ", has_on)

#check for s
s="I hope this course is not full of jargon"
has_jargon="jargon" in s
print("Has the word jargon? ", has_jargon)

has_on="on" not in "dragon" and "on" not in "python"
print("Doesn't have on? ", has_on)

#find length an convert
int_py=len("python")
float_py=float(int_py)
string_py=str(float_py)

print(int_py, float_py, string_py)

#check if een
num=int(input("Enter number: "))
rem= num%2
is_even=(rem==0)
print("Is the number even?", is_even)

#comparing equality
print(7//3 == int(2.7))
print(type(10)==type("10"))
print(int(9.8)==10)

#calculate earnings
hr=float(input("Enter hours: "))
r=float(input("Enter rate per hour: "))
earn=hr*r
print("Your weekly earning is ", earn)

#convert years to seconds
yr= float(input("Enter number of years you have lived: "))
secs=yr*365.25*24
print("You have lived for ",secs," seconds.")

#table with powers for each number from 1 to 5
for i in range(1,6):
    j=i
    print(i,"\t",1, end="\t")
    for p in range(2,5):
            print(j, end="\t")
            j=i**p
            p+=1
    print()

#OR

for i in range (1,6):
      row=[str(i)]
      for j in range(0,4):
            row.append(str(i**j))
      print(" ".join(row))
print()
