import json
fname =input("plz enter name")
lname = input("plz enter your lname")

inputdata= fname+":"+lname

# fobj = open("users.txt","w")
# fobj.write(inputdata)
d = {"firstname":fname, "lastname":lname}
print(d)

with open("users.json","r") as jf:
    data = jf.read()
    print(data)  # as a string
    # convert into dictionary
    # function loads
    dicdata = json.loads(data)
    # print(type(dicdata))
    print(type(dicdata["users"]))
    dicdata["users"].append(d)
    dicdata["users"].append(d)
    print(dicdata)

with open("users.json","w") as fw:
    json.dump(dicdata,fw,indent=2)