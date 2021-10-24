# Any program ---> Python
# 1- syntax error
# print("hii")
# 2- logical error -لا يكلف الله نفساً إلا وسعها-
# def sumfun(x,y):
#     return x *y
#
# print(sumfun(2,2))

#  runtime error
#print(name)  # exception ### must be handled ,
# try , except, else, finally block


# exception --> event which occurs during the execution of the program -->
# that disturbs the normal flow of the application
# exception object
# exceptions ---> Exceptions
# python raises ---> handle it , terminate the process
# print(name)
# name = "python "
# handing
try:
    print(name)
# except :
#     print("variable is not defined ")
except ValueError as e:
    # pass
    print(e)
except NameError:
    # pass
    print("plz define the variable first and try again")
except Exception:
    print("hello exception")
    pass
else:
    # will be executed if there no exception
    print("hi , this in no problem with this part")
finally:
    # will be executed if there are any exception ---
    print("I will be called anytime ")



print("After the explosion")

