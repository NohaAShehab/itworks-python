#
# age = 25
# status = ""
# if age < 13:
#     status = "kid"
# elif  13 <age < 18:
#     status= "teenager"
# else:
#     status = "adult"
#
# print(status)
# # shorhandif
#
# status = "kid" if age < 13 else "teenager" if age < 18 else "adult"
# # print(status)


# swap functions
# x = 10
# y = 5
# # print(x,y)
# # temp = x
# # x = y
# # y = temp
# # print(x,y)
#
# x,y = y,x
# print(x,y)
# join ,,,
# mylist = ("python", "shellscript", "django", "js")
# # join list items into one string
# liststring = ":".join(mylist)
# print(liststring)
#
# name = "Ahmed"  #  A@h@m@e@d
# print("@".join(name))

# x = [100]  # 1$0$0  # [100]
# print("$".join(str(x)))


# info = {"company":"itworks", "course":"python" }
# print(":".join(info))
#
# for char in "noha":
#     print(char)


##### split

# fullname = "Noha:Shehab"
# x = fullname.split(":")  # accept splitting delimeter return list of the parts
# print(type(x))  # retrun string into list


# is , in
l1 = ["Mohamed", "Zenia", "Rana", 0]
l2 = ["Mohamed", "Zenia", "Rana", 0]
# print(l1 == l2)  # check values inside list

# print(l1 is l2)   # compare reference , and values


# l3 = l4 = ["Mohamed", "Zenia", "Rana", 0]  # 2 references for the same variable
# print(l3 is l4)


# sequence unpacking
#
# mylist = ["python", "shellscript", "django","flask", "react","js"]
#
# a, *b, d = mylist  # starred item
#
# print(a,b,d)


# enums
# Enumerate () ---> method add counter to an iteratable and return it in form of enumarate object
# enumerate object can be used in for loops
# iterable with item
listt = ["python", "shellscript", "django","flask", "react","js"]
# counter with list
for i in range(6):
    print(listt[i])
#
# mylist= enumerate(listt)
# print(mylist)  #enumerate object 0x000001C31CB33C80
# print(type(mylist))
#
# # enumerate add counter to the object
# for i, item in mylist:  # counter start form zero
#     print(f"index  = {i} and item = {item} ")



# all, any
# check if all the values inside a seq, are evaluating to True  --> all

# listt = ("python", "shellscript", "django", "","flask", "react","js")
# # print(all(listt))
# l = ["", False, 0]
# # check if at least of of the values inside a seq, is evaluating to True  --> all
# print(any(l))


### print
#
# print("hello world", end=" ")  # print item, new line
# print("hi ")




