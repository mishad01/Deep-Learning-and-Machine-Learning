# Arithmetic Operations
# Operator Precedence
# Math Functions
# Indentation
# If Statements
# Logical Operators
# Comparison/ Relational/ Conditional Operators
# Assignment Operators
# Ternary Operators
# While Loops
# Break & Continue Statement
# Sum of n Numbers Program
# For Loops
# For-While Comparison
# For with Range Function
# Nested Loops


#Arithmetic Operations
var1 = 20
var2 = 10

print(var1+var2)
print(var1-var2)
print(var1*var2)
print(var1/var2)
print(var1//var2) #floor division. If we gen 2.3 then it will show 2
print(var1%var2)
print(var1**var2) #power (x^n)



#Math Functions/ Module
import math
x = 2.9;
print(round(x))
print(abs(-x))
print(math.ceil(x))
print(math.floor(x))



#IF ELSE
i = 8

if i<10:
    print(str(i)+" is less than 10" )
elif i>10:
    print(str(i) + " is grater than 10")
else:
    print(str(i) + " is equal to 10")



#NUMERIC DATA TYPE
#a+bi = (a is real)+(b is imaginary)(i = root -1)
a = 6+7j
print(a)
print(a.real)
print(a.imag)
print(type(a))
b = 5+5j
print(a+b)



# While Loop
#SUM OF NUMBERS PROGRAM
n = int(input("Enter the n number \n"))
sum = 0
i = 1

while i<=n :
    sum+=i
    i+=1
print(sum)

# While Break
i = 1
while i <6:
    print(i)
    if i==3:
        break
    i+=1

# While Continue
while i <6:
    i += 1
    if i==5:
        continue
    print(i)

sum = 0
while True:
    num = input("Enter a Number")
    if num =='quit':
        break;
    try:
        num = int(num)
    except:
        print("Enter a valid number please")
        continue
    sum+=num
    print(sum)


# For Loop
for x in "Banana":
    print(x)
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

#For Continue
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == 'banana':
        continue
    print(x)
#For Break
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == 'banana':
     break
    print(x)

##For with Range Function
#Using the range() function:
for x in range(6):
 print(x)

 # Using the start parameter:
for x in range(2, 6):
    print(x)


# Increment the sequence with 3 (default is 1):
# 2 is the starting value, 30 is the end value (exclusive)
# 3 is the step value, which increments the sequence by 3 at each step.
for x in range(2, 30, 3):
 print(x)


#For with Enumerate
num = [30, 10, 70, 121]
for i, x in enumerate(num):
 print(i, x)

#Nested For Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
 for y in fruits:
  print(x, y)