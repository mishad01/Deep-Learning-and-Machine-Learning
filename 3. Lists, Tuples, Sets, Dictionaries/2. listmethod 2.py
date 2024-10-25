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
