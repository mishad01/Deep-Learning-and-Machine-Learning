range_value = range(0,5,2) #Basically (i = 0;i<n;i++)
for i in range_value:
    print(i)

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