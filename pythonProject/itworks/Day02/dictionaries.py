# dictionay in other programming lang. ---> Associative arrays

# doesn't use index but key-value pairs

# mutable data structure  ---> Key:value pairs , separted by comma, ---> in cruly braces

d = {} # empty dictionary
print(type(d))

# keys --> doesn't allow duplicates for keys
info = {"name": "Noha", "email": "nshehab@iti.gov.eg"}
print(info)
# access element using keys
print(info["name"])
# dictionary is mutable datatype
info["name"]= "Noha Shehab"  # check if key exists  --> update item
print(info)
# add new item
info["age"]= 29
print(info)

# dictionary values from 3.7 ---> items of dictionary are stored ordered
print(len(info))

# get keys

print(list(info.keys()))
# get values
print(list(info.values()))
# get items
print(info.items())

# d2 = {"work":"iti", "course":"python", "name":"noha"}
#
# # info.update(d2)
# # print(info)
#
# d2[5]='test'  # as a key
# print(d2)
#
# d2[3.7]='test'  # as a key
# print(d2)
#
# d[True] = "abc"
# print(d2)
info = {"name": "Noha", "email": "nshehab@iti.gov.eg", "course": "python"}

# check key exists in dictionary
if "name" in info:  # check the keys
    print("hi")
else:
    print("bye")

# check values
if "python" in info.values():
    print("hi")
else:
    print("bye")


# loop over the dictionary
for item in info:
    print(f"{item} = {info[item]}")


for key,value in info.items():  # list of tuples
    print(f"{key} = {value}")


# remove all items in dictionary

info.clear()
print(info)

del(d)


# sort dictionary items or not 