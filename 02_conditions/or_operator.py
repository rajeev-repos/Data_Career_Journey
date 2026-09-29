student_id = input("Do you have a student ID (yes/no): ").lower()
entry_pass = input("Do you have an entry pass (yes/no)").lower()

print(student_id == "yes" or entry_pass == "yes")