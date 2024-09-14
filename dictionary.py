dict={
    "Sagar": "Human being",
    "Laptop": "Object"
}
print(dict["Sagar"])
print(dict["Laptop"])


# example of dictionary
info={'name': 'sagar', 'age':'22','elgible':'12'}
print(info)
print(info["name"])


# not found key then print none value
print(info.get('name2'))

for key in info.keys():
    print(info[key])
print(info.items())    
print(info.values())

# update method in dictionary

ep1={122:45,243:78,324:68,846:70}
ep2={323:78,348:88,874:80}
# ep1.update(ep2)
# ep1.clear()
# ep1.pop(122)
# ep1.popitem() last dictionary value delete
print(ep1)