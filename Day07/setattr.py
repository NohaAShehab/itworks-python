class Person:
    pass


p = Person()
p2 = Person()
# print(p)
# # loosly dynamically typed lang
# p.name = "Ahmed"
# print("test")
# set attribute --> add attribute in the runtime
# attr1 = "firstname"
# attrval = "Rana"
# setattr(p, attr1, attrval)
# print(getattr(p,attr1))
# # p.firstname = "Rana"
# # p.fname ="rana"
# # p.email = "rana@itiworks.com"
#
# print("test")

# set attr, values --> you want to add it the object
p = Person()
# do fill p objecy with info data
info = {"name":"Zenia", "dept":"python", "company":"itworks"}

for key, value in info.items():
    setattr(p,key,value)

print("test")
print(p)
print("test")