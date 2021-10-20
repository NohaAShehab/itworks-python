# deifne any variable --->

# global scope

# name = "Rana"  # global scope  --> global variable
#
# def outerfunction(): # name, is defined in the paramter scope  --> local scope inside function
#     global name
#     name ="Ali"
#     email = f"{name}@itworks.com"  # local variable  --> local scope
#     print(f"outer function {name}, {email}")
#     # inner function
#     def printfun():  # local scope inside the function
#         global name
#         name = "Ahmed"  # define new local variable with name name
#         print(f"inner {name}")
#     printfun()
#     print(name)
#
# outerfunction()
# print(name)


year = 2021  # global variable can be printed from any part,

def happynewyear():
    # year =2022
    # print(year)
    global year
    year = 2022
    day = "Tuesday"
    def inner():
        print(year)
    inner()



happynewyear()

