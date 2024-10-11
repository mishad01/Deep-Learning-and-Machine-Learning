#LISTS
thislist = ["Apple","Banana","Cherry","Apple"]
list1 = [1,2,3,4,5]
list2 = ["a",1,"ds",4]
print(thislist)
print (list1)
print (list2)

listl = ["Apple", "Banana", "Cherry", "Mango", "Guava"]
print(listl[0:2])
print(listl[-3:-1])
print(listl[0:5:2]) #the last 2 is, if it gets even it will remove that element

print(listl[1]*3)  #Banana Banana Banana
print(listl + ["tomato", 50]) #Add

#List Methods
'''
append() = Adds an element at the end of the list
clear() = Removes all the elements from the list
count() = eturns the number of elements with the specified value
extend() = dd the elements of a list (or any iterable),to the end of the current list
index() = Returns the index of the specified value.
insert() =Adds an element at the specified position.
pop() = Removes the element at the specified position.
remove() = Removes the first item with the specified value
reverse() = Reverses the order of the list
sort() = Sorts the list
'''
print("----- List Method----")
fruits = ['apple', 'banana', 'cherry', 'orange']
fruits.append('mango')
#fruits.clear()
x = fruits.count('cherry')
#print(x)
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars) #Sums Two Array
print(fruits.index("banana"))
fruits.insert(1,"asd")
fruits.pop()
fruits.remove('asd')
fruits.reverse()
fruits.sort()
print(fruits)

#List Unpack
testlist = ['a','b','c']
item1,item2,item3 = testlist
print(item1)
print(item2)
print(item3)

first_item, *rest_of_the_items = testlist  # * means rest of the value
print(first_item)
print(rest_of_the_items)

first_item,second_item, *rest_of_the_items = testlist  # * means rest of the value
print(second_item)

new_list = [
    *testlist, # if we use * we are basically breaking the whole thing
    "peyaj",
    "roushun"
]
print(new_list)

#List & Tuple Compare in Python

a = [5,6,25,51]
b = [8,9,18,46,25]

if(a>b):
    print("a is bigger")
else:
    print("b is bigger")


# 2D Matrix

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[0])

# TUPLE -> Tuple is Unchangeable
listTuple = ('a','b',1,2,3)
print(listTuple)

x = ("a","b")
first,scond = x
print(first)
# print(second)

#Sets in Python => Partially Unchangeable, Unindex and Unique

set = {1,2,3}
set2 = {1,2,3,3}  #similar element will be removed
set3 = {"apple","banana","barry"}
print(set3)

# Set Operations in Python
num1 = {1,2,3,4,5}
num2 = {4,5,6,7}

print("Union")
print(num1 | num2) #Union
print(num1.union(num2)) #Union

print("Intersection")
print(num1 & num2) #Intersection
print(num1.intersection(num2)) #Intersection

print("Intersection")
print(num1 - num2) #Intersection
print(num1.difference(num2)) #Differnce

for fruit in fruits:
    print(fruit)

index = 0
while(index<4):
    print(fruits[index])
    index+=1

#Dictonary In Python
student = {
    "name" : ["Mishad","Mahia"],
    "id":"221000412",
    "semester":"9th",
    "ischeck":"true"
}

student.update(
    {
    "home":"dhaka",
    "interest":"cse"
    }
)
print(student.get("ischeck",False));
for item in student.items():
    print(item)

for item in student.keys():
        print(item)
for item in student.values():
    print(item)

for item in student.items():
    print(item)

for key, value in student.items():
    print("Key: ",key)
    print("Value",value)


#For loop
range_value = range(0,5,2) #Basically (i = 0;i<n;i++)
for i in range_value:
    print(i)

#Practice Problem (Shopping List Manager)
# shoppingList =[]
# while True:
#     a = input("Add an item to the shopping list (or type 'done' to finish): ")
#     if a.lower() == "done":  # Check if the input is 'done'
#         break
#     else:
#         shoppingList.append(a)
# print("\n")
#
# print(shoppingList)
# for i,item in enumerate(shoppingList,1):
#     print(f"{i}. {item}")
# print(f"\nTotal number of items: {len(shoppingList)}")

#Score Tracker
'''You are asked to create a Score Tracker. YoWll
take the name and the score of a student as
input. Store those by name and print all the
student's names with their scores. The input
ends when the student's name is "stop"'''

students = []

while True :
    name = input("Input Name : ")
    if(name=="stop"):
        break
    else :
        score = input("Input Score :")
        student = {
            "name": name,
            "score": score
        }
    students.append(student)

print(students)

for x in students:
    print(f"{x['name']} : {x['score']}")
