

# file --->  direct access to the avaiable stroge
# read data , write data
# how to use external storge ....
# server direct --> deal file

# 1-open file
# open (filename as string, filemode) filemode, read, write
try:
    fileobject = open("notes4.txt", "r") # default mode is read
except Exception as e:
    print(e)
else:
    print(type(fileobject))
    print(fileobject.name)
    print(fileobject.mode)
    print(fileobject.closed)
    # built in function --> open

    # 2- perform operation read or write
    # data  = fileobject.read()  # return with text inside file into str
    # print(type(data))
    # print(data)

    # data = fileobject.read()  # return with all text inside file into str
    # # print(type(data))
    # print(data)

    # read line by line
    # data = fileobject.readline()  # first line
    # print(data)
    # data = fileobject.readline()  # first line
    # print(data)
    # data = fileobject.readline()  # first line
    # print(data)
    # data = fileobject.readline()  # first line
    # print(data)
    # data = fileobject.readline()  # first line
    # print(data)
    # fileobject.seek(10)
    # newdata = fileobject.read()
    # print(f"data: {newdata}")

    lines = fileobject.readlines()
    print(type(lines))
    print(lines)

    # 3-close
    fileobject.close()
