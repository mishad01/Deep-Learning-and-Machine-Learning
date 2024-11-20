#1. Reverse and concat two list
a = ["book",1,"him",23,64,"Tour"];
b = ["hello","its","me"];
print(a+b);

#2. 2 Remove duplicate items from the list
a = ["book",1,"him",23,64,23,23,23,"Tour","him"];
b = []
for i in a:
    if(i in b):
        continue
    else:
        b.append(i)

print(b)

#another way
a = ["book",1,"him",23,64,23,23,23,"Tour","him"];
b = list(set(a))
print(b)

#3. Swapping
