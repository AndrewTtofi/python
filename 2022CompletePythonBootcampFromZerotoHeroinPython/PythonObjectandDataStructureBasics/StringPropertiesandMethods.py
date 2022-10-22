name = 'Sam'
#name[0] = 'P' -> not good, strings are immutable objects (cannot be changed)

last_letters = name[1:]
x = 'P' + last_letters
print(x)


y='Hello World'
print('This is first y',y) 
y = y + ' it is beatiful outside'
print ('This is second y',y)
