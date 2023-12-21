import json

#read the json file
with open("data.json", "r") as f:
    data  = json.load(f)

with open("data.json","w") as f:
    json.dump(data,f , indent=3, sort_keys=True)

with open("data1.json","w") as f:
    old= json.dump(data,f, indent=3, sort_keys=True)

with open("data1.json","r") as f:
    old = json.load(f)
    print(old)


# add new key-value to data1.json
with open("data.json","r") as f:
    new=json.load(f)   
    new["language"]  = "python"

with open("data.json", "w") as f:
    json.dump(new,  f , indent=4  , sort_keys=True)

