# python support functional programming
# must be generic --> Don't ever never repeat
# function first of way of scoping
# function is a block of organized, reusable code --> that is used to perform single action ,
# function --> provide modularity , reusing

# def function

def functioname(param=""):
    return


# you must define the function before calling,

# def greetfunction(name):
#     print(f"hello world {name}")
#     return
#
# x = greetfunction(["itworks"])
# print(type(x), x)


# def changeitem(mylist):
#     # scoping
#     mylist = [1,2,3,5]
#     print(mylist)
#     return
#
#
# mylist = ["a","b","c","d"]
# changeitem(mylist)
# print(mylist)


# fuction parameters
# 1- order doesn't matter
# 2- no specefic datatype
# 3- add default value


# def printinfo(email, name="user"):
#     print(f"{name}  , {email} ")
#
#
# printinfo("ali", "ali@itworks.com")
# printinfo("test")

# return statment
# def mulfn(x,y):
#     return str(x*y)
#
# print(mulfn(4,5))

# define function with know number of parameters

# I don't know the number of parameters ,,,,
# * argument

# def abc(*items):   # items count can be zero or more
## items will be stored inside in a tuple
#     print(items[3])
#     print(type(items))
#     for item in items:
#         print(item)
# abc(4,6,6,77,777,"gfd", True, [5,6,7], {"name":"noha"})

# abc(name="ahmed", email="ali")

def printinfo(**test):
    # parameters 000--> storing inside dic ----
    print(test)
    print(type(test))
    for key in test:
        print(f"{key}:" + "{"+ f"{test[key]}"+"}")
        print(f"{key} {test[key]}")
        # .format

printinfo(_="python",year=2021, company="itworks")


# diccc = {1:"Ahmed", "age":20}
# print(diccc)

# printinfo(name="rana", faculty="Engineering", spec="Communication")

# printinfo(5)


# return

temp = 37

def testtem(temp):
    if temp > 25:
        return "hot"
    elif temp == 25:
        return "fine"

    print("testtt")
    return "not found"
    # print("this a line after return")



print(testtem(temp))
