##User Function
#1
def my_function():
    print("Mishad")
    print(5+5+5)

my_function() #Function Call

#2 parameter is basically variable
def my_function(fname): #
    print("Good morning!", fname)

my_function("Sakif")

def check(a):
    if(a==1):
        return True
print(check(1))

#3 Argument
def add(a,b):
    print(a+b)

add(5,5)


##Keyword Parameters/Arguments

def my_fun(child1,child2,child3):
    print("The Youngest child is :",child3)

my_fun(child1="Sakif",child2="Rahaman",child3="Mishad")

#Deafult Parameter Value (It can be change later also)
def my_function(country = "Norway"):
    print("l am from u", country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#Docstring -> Comment inside docstring
def addDocString(a,b):
    '''This will take two parameter
    Return Value is integer'''
    return  a+b
print(addDocString(5,5))
print(addDocString.__doc__)

#Lambda Function
'''lamda function = anonymous function '''
''' here (lamda a = parameter)
(a+10 = expression)
Python Lambda Functions are anonymous function means that the function is without a name.
'''
x = lambda a : a+10
print(x(5))

x = lambda a,b,c : a+b+c+10
print(x(5,5,5))

def cube(y):
    return  y*y*y
print(cube(5))
cubeLamda = lambda y : y*y*y
print(cubeLamda(7))

##Map and Filter function

def checkLen(a):
    return len(a)

x = map(checkLen, ('apple', 'banana', 'cherry'))
print(list(x))

age =[5,2,7,8,3,25]

def checkValue(x):
    if(x<5):
        return False
    else:
        return  True

adults = list(filter(checkValue,age)) #Filers return true value
print(adults)

def square(x):
    return x*x

num = [1,2,3,4,5]
result = list(map(square,num))
print(result)
num = [5, 12, 17, 18, 25, 32]
result = list(filter(lambda x : x%2==0,num))
print(result)
print(num)

text = input("Enter: ")
nums = text.split()

print(nums)
