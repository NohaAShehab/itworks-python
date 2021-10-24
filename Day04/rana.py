import re
import datetime


def validatemail():
    while True:
        email = input("Please Enter your email ")
        if len(email) != 0 and re.search('^[a-zA-z]+[._]?\w+[@]\w+[.]\w{2,3}$', email):
            info.append(email)
            return email


def validatepassword(password):
    return len(password) >= 8


def validateName(name):
    while True:
        Name = input(f"Please Enter your {name} name ")
        if Name.isalpha() and len(Name) != 0 and not Name.isspace():
            return info.append(Name)


def validateMobile():
    while True:
        mobile = input("Please enter your mobile number")
        if len(mobile) == 11 and mobile.isdigit() and re.search('^01', mobile):
            return info.append(mobile)


def createProject():
    project = []
    while True:
        projecttName = input("Please Enter the project title ")
        if projecttName.isalpha() and len(projecttName) != 0 and not projecttName.isspace():
            project.append(projecttName)
            break
    while True:
        projectdetails = input("Please Enter the project details ")
        if len(projectdetails) != 0 and not projectdetails.isspace():
            project.append(projectdetails)
            break
    while True:
        target = input("Please Enter the project's target ")
        if len(target) != 0 and not target.isspace():
            if re.search('\d+\.?\d*', target):
                project.append(float(target))
                break
    while True:
        projectStart = input("Please Enter the project start date  ")
        projectend = input("Please Enter the project end date  ")
        if len(projectStart) != 0 and not projectStart.isspace() and len(projectend) != 0 and not projectend.isspace():
            project.append(projectStart)
            project.append(projectend)

            break

    print(project)


def writeToFile(f, infolist):
    try:
        fileobject = open(f, "a")
    except Exception as e:
        print(e)
    else:
        for element in infolist:
            fileobject.write('%s ' % element)
        fileobject.write('\n')


def readFile(f):
    try:
        fileobject = open(f)
    except Exception as e:
        print(e)
    else:
        return fileobject.readlines()


def searchFile(f, searchItem):
    print("in")
    fileContent = readFile(f)
    if f == "registeration.txt":
        email, password = searchItem
        for line in fileContent:
            if email == line.split()[2] and password == line.split()[3]:
                print("found")
                break
        else:
            return False


def test(f, S):
    print(f, s)


print("----- Authentication System -----")
info = []
while True:
    ans = input("Enter 1 to register or 2 to login ")
    if ans == "1":
        validateName("first")
        validateName("last")
        validatemail()
        while True:
            password = input("Please enter your password ")
            if validatepassword(password):
                confirmpassword = input("Please confirm your password ")
                if password == confirmpassword:
                    info.append(password)
                    break
                else:
                    print("Passwords don't match")
            else:
                print("Weak password")
            print("Try again")

        validateMobile()
        writeToFile("registeration.txt", info)
        break
    elif ans == "2":
        while True:
            if validatemail():
                password = input("Please enter your password ")
                if validatepassword(password):
                    print("in")
                    # searchFile("registeration.txt",[validatemail(),password])
                    test("registeration.txt", [validatemail(), password])
                    # createProject()
                    break
                else:
                    print("Invalid password")
            print("Try again")

        break
    else:
        continue

