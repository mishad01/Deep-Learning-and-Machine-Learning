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