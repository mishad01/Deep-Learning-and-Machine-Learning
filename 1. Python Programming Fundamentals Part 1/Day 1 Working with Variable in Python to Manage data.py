#The Python Input Function
#print("Hello " + input("Whats Your Name?\n")+"!")

# Python Variables
name = "Mishad"
length = len(name)
age = 22
print(len(name))
print(name,age,length)

# Coding Exercise 3: Variables
'''We have 2 variables glass1 and glass2. glass1 contains milk and glass2 contains juice.
Write 3 lines of code to switch the contents of the variables.
You are not allowed to type the words "milk" or "juice".
You are only allowed to use variables to solve this exercise'''

glass1 = "milk"
glass2 = "juice"

a = glass1
glass1 = glass2
glass2 = a

# 11. Day 1 Project: Band Name Generat
print("Welcome to Brand Name Generator")
city =  input("Which city did you grow up in? \n")
pet = input("What is the name of a pet?\n")
print("Your Brand Name could be: "+ city+" "+pet)

