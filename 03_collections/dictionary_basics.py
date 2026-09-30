#keys/values/items
stu = {
    "Name": "Rajeev",
    "Age": 30,
    "City": "Nepalgunj",
    "Country": "Nepal"

}

print(stu)
print(type(stu))

print(stu["Name"])
print(stu["Age"])
print(stu["City"])

stu["Age"] = 80
print(stu)

print("--------Break---------")

print(stu.keys())
print(stu.values())
print(stu.items())