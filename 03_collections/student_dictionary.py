stu = {
    "Name": "Rajeev Subedi",
    "Course": "BE",
    "College": "Shikha Academy",
    "Marks": 85,
    "Attendance": 75
}

print(stu.items())
print(stu["Name"])
print(stu["Marks"])

stu["Result"] = "Pass"

print(stu.items())
print(stu.values())

stu.pop("Name")
print(stu.items())

