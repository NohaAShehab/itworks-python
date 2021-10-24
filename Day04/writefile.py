try:
    fileobject = open("users.txt", "a")
    # file not found will create it
    # override the existing data within file
    # append mode
except Exception as e:
    print(e)
else:
    fileobject.write("yes first line \n")
    fileobject.write("yes first line \n")
    # fileobject.seek(30)  # byteees
    # fileobject.write("hiiiii")
    fileobject.write("yes first line \n")
    fileobject.writelines(["abc\n", "test\n", "noha\n","Mohamed\n", "Zeina\n", "Rana\n"])

    fileobject.close()
finally:
    pass