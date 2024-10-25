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
