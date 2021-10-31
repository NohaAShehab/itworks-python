# json --> javascript object notation   --> store data
# lightweight - data interchange format
# independent of js

# rising business --> web scraping --> ==3 read their info in form json

# deal with json data--> files, website
# data from file
import json
jsonfile = open("test.json")
print(jsonfile)
data = jsonfile.read()  # read json data into string
# print(type(data))
# deal with json
# load data from string into json format

# jsondata = json.loads(data)  # load the data from string contains json into dictionary
# print(type(jsondata))
# print(jsondata["students"])
# for item in jsondata["students"]:
#     print(item)
# print(len(jsondata["students"]))
# write json data in file
print(data)
with open("newfile.json","w") as fjson:
    # fjson.write(data)

    # write json object into a file
    # read string into json
    newdata = json.loads(data)
    json.dump(newdata,fjson)
    # then write json again

# read data from json file
with open("newfile.json", "r") as rjson:
    jdata = rjson.read()
    d = json.loads(jdata)
    print(jdata)
    # mydata = json.dumps(jdata,indent=2)
    print(json.dump(d,indent=2))  # convert json object into ---> python dic




