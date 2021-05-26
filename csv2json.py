import json
import pandas as pd

data = {}

df = pd.read_csv("dataset.csv")

result = df.to_json(orient="records")
prev = json.loads(result)
for i in prev:
    field = str(i['Nombre'])
    data[field] = i


s = json.dumps(data, indent=4)

with open("json/metadata.json","w") as f:
    f.write(s)