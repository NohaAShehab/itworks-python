# tuple
# sequence ---> immutable datatype--> once created You cannot change it
# Tuple like list ---> immutable ---

t = tuple([4,5,"test"])
print(t)

t2 = ("Mohamed", "Zenia", "Rana")
print(type(t2))

# tuple doesn't support item assignment
print(t2[2])
# t2[2]="Test"
# tuple cannot be updated
t1 = ("python", "Postgres", "Java")  # like constant
t2 = ("js", "react", "es6", "nextjs")
t3 = t1 + t2
# print(t3)
#create tuple of one item
unit = ("item",)
print(type(unit))

# # del(unit)
# del unit
# print(unit)

# iteration
# for item in t3:
#     print(item)

# find item in tuple
# in- operator  --> memebership
# print("python" in t3)

t4 = (55,66,77)
print(min(t4))

print(len(t4))
