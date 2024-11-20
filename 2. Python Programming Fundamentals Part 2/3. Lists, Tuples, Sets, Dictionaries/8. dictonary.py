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