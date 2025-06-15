from string import digits, ascii_letters
from random import randint


def user_generator():
    alphanum=digits+ascii_letters
    id=""
    for i in range(6):
        r=randint(0, len(alphanum)-1)
        id+=alphanum[r]
    return id

print(user_generator())



def user_id_gen_by_user():
    char_no=int(input("Enter number of characters: "))
    user_no=int(input("Enter number of user ids: "))
    alphanum=digits+ascii_letters
    ids=[]
    for j in range(user_no):
        id=""
        for i in range(char_no):
            r=randint(0, len(alphanum)-1)
            id+=alphanum[r]
        ids.append(id)
    return ids

#print(user_id_gen_by_user())


def rgb_color_gen():
    col1=randint(1,255)
    col2=randint(1,255)
    col3=randint(1,255)
    color=(col1, col2, col3)
    return color

#print(rgb_color_gen())


def list_of_hexa_colors (n):
    chars=digits+ascii_letters[:6]
    colors=[]
    for j in range(n):
        color='#'
        for i in range(6):
            rand=randint(0, len(chars)-1)
            color+=chars[rand]
        colors.append(color)
    return colors

print(list_of_hexa_colors(5))


def list_of_rgb_colors (n):
    colors=[]
    for j in range(n):
        col1=randint(1,255)
        col2=randint(1,255)
        col3=randint(1,255)
        color='rgb({},{},{})'.format(col1, col2, col3)
        colors.append(color)
    return colors

print(list_of_rgb_colors(3))

def generate_colors(col_type, n):
    if col_type=="hexa":
        return list_of_hexa_colors(n)
    elif col_type=="rgb":
        return list_of_rgb_colors(n)
    else:
        return "Invalid color type"
    
print(generate_colors("hexa", 5))

def shuffle_list(l):
    shuffled=[]
    for j in range(len(l)):
        i=randint(0,len(l)-1)
        shuffled.append(l[i])
        l.remove(l[i])
    return shuffled

print(shuffle_list([1,2,5,3]))


def return_array():
    arr=[]
    digs=list(digits)
    for i in range(7):
        r=randint(0,len(digs)-1)
        arr.append(int(digs[r]))
        digs.remove(digs[r])
    return arr

print(return_array())