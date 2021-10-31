import json

# with open("students.json") as f:
#     data =f.read()# str
#     dicdata = json.loads(data)
#     print(type(dicdata))
#     name = input("plz enter your name ")
#     email = input("plz enter your email ")
#     info = {"name":name, "email":email}
#     print(type(dicdata["students"]))
#     dicdata["students"].append(info)


# with open("students.json","w") as fw:
#     json.dump(dicdata,fw, indent=2)


# search in json file

with open("students.json") as f:
    data =f.read()# str
    dicdata = json.loads(data)
    print(type(dicdata))
    name = input("plz enter your keyword ")
    print(dicdata)
    for item in dicdata["students"]:
        if item["name"] == name:
            dicdata["students"].remove(item)

    print(dicdata["students"])
