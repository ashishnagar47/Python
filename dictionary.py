my_dict={}

dict={
    "name":"ashish",
    "role":"cybersecurity",
    "city":"delhi"
}

print(dict.get("role")) 

print(dict.keys())
dict.update({"shdjk":"skjd"})
print(dict)

for keys in dict.keys():
    print(keys)

for values in dict.values():
    print(values)

for keys,values in dict.items():
    print(keys,values)