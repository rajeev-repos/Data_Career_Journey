first_name = "Rajeev"
last_name = "Subedi"
print(first_name)
print(type(first_name))
print(last_name)
print(type(last_name))

#Joining strings
full_name = first_name + "" + last_name

#Length
print(len(full_name))

#Change Case
print(full_name.upper())
print(full_name.lower())
print(full_name.title())

#Access characters
print(full_name[0])
print(full_name[-1])

#Slicing
print(full_name[0:6])

message = " I am Learning Python "

print (message.strip())
print(message.replace("Python", "Programming"))
print("Python" in message)

print(message.startswith("I"))
print(message.endswith("Python"))
print(message.count("n"))
print(message.find("Python"))

