print("Hello World")




#defining variables
z, y, x = "Melina", "Andreas", "Dimitrakis"
print(y,z,x)


#or create a list with the variables and then unpack it. This method is called UNPACKING
names = ["Melina", "Andreas", "Mina"]
b, c , p= names
print(b,c,p)

#To combine both text and a variable, Python uses the + character:
e = "awesome"
print ("Python is "+ e)


def myfunction():
    global o
    o = "ok"
    print("Python is not " + e)

myfunction()

print("python is ",o)