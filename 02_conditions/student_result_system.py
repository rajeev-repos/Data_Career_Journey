name = input("Enter Student name: ")
marks = int(input("Enter Student's obtained marks: "))
attendance = int(input("Enter attendance percentage: "))

print("--------------- STUDENT RESULT --------------- ")
print("Student: ",name)
print("Marks: ",marks)

if marks<=100 and marks>=80:
    print("Grade: Distinction")
elif marks <80 and marks>=60:
    print("Grade: First Division")
elif marks<60 and marks>=40:
    print("Grade: Pass")
elif marks<40 and marks>=0:
    print("Grade: Fail")
else:
    print("Grade: Invalid Marks")

if attendance <= 100 and attendance >= 75:
    print("Attendance: Eligible")
else:
    print("Attendance: Not Eligible")

if (marks<=100 and marks >=40) and (attendance >= 75 and attendance<=100):
    print("Final Result: PASS")
elif (marks<=100 and marks >=40) or (attendance >= 75 and attendance<=100):
    print("Final Result: FAIL")
else:
    print("Final Result: Invalid Credincials")
    
