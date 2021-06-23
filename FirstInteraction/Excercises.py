"""
example excercises for Python
Link:
https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
"""
#Exercise 1
print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")


#Exercise 2
import sys
print("Python Version")
print(sys.version)
print("Version info.")
print(sys.version_info)

#Excercise 3
import datetime
print("Current Date and Time:")
now = datetime.datetime.now()
print (now.strftime("%Y-%m-%d %H:%M:%S "))

#Excercise 4
import math
p = math.pi
r = int(input("Hello Please enter Radius: "))
area = p * (r*r)
print("the Area of the circle is ",area)

#Excercise 5
surname=input("Please enter your surname: ")
firstname=input("Please enter your first name: ")

print("This is your name: \n", surname + firstname )

#Excercise 6
values = input("Insert comma seperated values: ")
listvalues = values.split(",")
tupleofvalues = tuple(listvalues)
print("The List: " ,listvalues)
print ("The Tuple: ", tupleofvalues)

#Excercise 7
filename=input("Input the name of file: ")
f_extension=filename.split(".")
print("The extension of the file is " + repr(f_extension[-1]))
"""
#Excercise 8
listseven = ("Red", "Green", "White", "Black")
print(listseven[0], " ", listseven[3])

#Excercise 9
exam_st_date = (11, 12, 2021)
print(exam_st_date[0],"/", exam_st_date[1], "/", exam_st_date[2])
    #or you can do the following
for i in exam_st_date:
    if  i<2:
        print(i, end =" ")
    else:
        print(i)