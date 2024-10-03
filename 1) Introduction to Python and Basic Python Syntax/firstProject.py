a = 10
b = 20
print(a+b)

print('Input Value')
x= input()
y = input()
print(x,y)

"""Two types of type conversion:
• Explicit Conversion (Manual Conversion)
• Implicit Conversion (Automatic Conversion)"""

#Explicit Conversion (Manual Conversion)
a = 15
b = 'mishad'
print(type(a))
print(type(b))

# Implicit Conversion (Automatic Conversion)
a = 15
print(type(a))
b = a+3.14
print(type(b))

#String in Python
str = "Hello World"
print(str[0]) #H
print(str[0:5]) #Hello
print(str[6:]) #world

#Swap Number
a, b = map(int, input('Swap Number :\n').split())
c = a
a = b
b = c
print(a, b)