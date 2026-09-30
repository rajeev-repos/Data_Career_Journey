subjects = ("Python", "SQL", "Power BI", "Excel")

print(subjects)
print(type(subjects))
print(len(subjects))

print(subjects[0])
print(subjects[-1])
print(subjects[1:3])

# list is mutable but tuple is not mutable
subjects[0] = "Java"