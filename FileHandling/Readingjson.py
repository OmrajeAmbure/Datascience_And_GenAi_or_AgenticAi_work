import json
with open("demojson.json", "r") as jsonfile:
    data = json.load(jsonfile)
    print(data[0]['name'])
    print(data[0]['rollno'])
    print(data)

# json like we have dictonary in python
jsontext = {
    "name":"omraje",
    "rollno":"01"
}

jsonfile.close()