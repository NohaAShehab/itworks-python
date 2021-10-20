# The most basic data structure in python ---> sequence
# sequence --> each element is assigned to a number --> start form 0 ---> represent its position or index
# python ---> has 6 built-in types of sequences -->
# most common sequences --> lists , tuples
# list --> the versatile datatype available in python -->
l = list([5, 6, 7])
l2 = ["iti", "itworks", "python", "databases"]
# list ---> varaible size
# can hold data with different datatypes
l3 = ["a", 5, "test", True, l]
print(l, type(l2))
print(l3)

# pop the last item
# print(l3.pop())  # return with removed it
# print(l3)  #
#
# # pop item at certain index
# l3.pop(2)
# print(l3)

# append
l3.append("itworks")
print(l3)

# insert into certain index
l3.insert(4,"python")
print(l3)

# extend
l4 = ["Zeina", "Rana", "Mohamed"]
l3.extend(l4)
print(l3)

# everything is an object
# list object ---> common function len

print(len(l3))

# cocatination
m = ["abc", True, 40 ,66]
n = ["ff", "test", "iti", 88]
z = m + n
print(z)

# repetition
ll = ["itworks"]* 5
print(ll)

# membership
l4 = ["Zeina", "Rana", "Mohamed"]

print("mohamed" in l4)

# iteration
# for loop
for item in l4:
    print(item)

# lists are not iterable --->

# list of integers or floats ---> min , max
x = [5,66,77]
print(min(x))

# empty lists
l = []

if l:
    print("abc")
else:
    print("nooo ")


z = ["abc", 55, 67]
print(z[2])


# list are mutable datatypes  ---> can be changed during execution
names = ["Mohamed", "Rana", "Zeina"]
# names[3] = "fff"
names.append("Noha")
# pop ---> last item ---> pop with index

# remove item
names.remove("Noha")
print(names)

print(names)
# tuple


# sorting --? list items