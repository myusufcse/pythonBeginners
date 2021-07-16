import json

s = ""
with open("data.json","r") as f:
    s = f.read()

print(s)
print(type(s))
s = json.loads(s)
print(type(s))
print(s["tom"])
