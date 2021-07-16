data = {}
data["tom"] = {
    "phone":456789,
    "name":"tom",
    "address":"1210 sjtn"
}
data["bob"] = {
    "phone":98765,
    "name":"bob",
    "address":"1000 brss"
}
print(data)
import json
s = json.dumps(data)
print(s)
with open("data.json", "w") as f:
    f.write(s)