import json

f = open("json/metadata.json")

s = f.read()

data = json.loads(s)

for i in data:
    if "moabb" in data[i]['Nombre']:
        s = json.dumps(data[i], indent=4)
        direction = "json/moabb/" + str(data[i]['Nombre']).replace(" ","_")+".json"
        with open(direction, "w") as f:
            f.write(s)
print("done")