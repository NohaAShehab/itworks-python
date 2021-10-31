import json

with open("test.json") as f:
    data = f.read()
    jdata = json.loads(data)
    print(jdata)

    for item in jdata["students"]:
        del item["Address"]
        item["sal"] = 1000

    print(jdata)
