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