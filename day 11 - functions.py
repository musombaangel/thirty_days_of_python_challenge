def add_two_numbers(num1, num2):
    return num1+num2

print(add_two_numbers(1,5))


def calc_area(radius):
    area=3.14*radius*radius
    return area

print(calc_area(1.5))


def is_numeric(object):
    return isinstance(object, (int, float, complex))

def add_all_nums(*nums):
    total=0
    for num in nums:
        if is_numeric(num):
            total+=num
        else:
            return "No meaningful output"
    return total
print(add_all_nums(1,2,"la"))
print(add_all_nums(1,2,3,4))


def convert_celsius_to_fahrenheit(c):
    F=(c*9/5)+32
    return F

print(convert_celsius_to_fahrenheit(52))


def check_season(month):
    if month=="September" or month=="November" or month == "October":
        sn="Autumn"
    elif month == "March" or month == "April" or month == "May":
        sn = "Spring"
    elif month == "June" or month == "June" or month == "July":
        sn = "Summer"
    elif month == "December" or month == "January" or month == "February":
        sn = "Winter"
    else:
        sn="Invalid. Not a real month or if it is, start with a capital letter. "

print(check_season("November"))


def calculate_slope(x1,y1,x2,y2):
    slope=abs(y1-y2)-abs(x1-x2)
    return slope

print(calculate_slope(8,3,1,4))

