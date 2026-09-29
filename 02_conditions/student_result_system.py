name = input("Enter Student name: ")
marks = int(input("Enter Student's obtained marks: "))
attendance = int(input("Enter attendance percentage: "))

print("--------------- STUDENT RESULT ---------------")
print("Student:", name)
print("Marks:", marks)

if 80 <= marks <= 100:
    print("Grade: Distinction")
elif 60 <= marks < 80:
    print("Grade: First Division")
elif 40 <= marks < 60:
    print("Grade: Pass")
elif 0 <= marks < 40:
    print("Grade: Fail")
else:
    print("Grade: Invalid Marks")

if 75 <= attendance <= 100:
    print("Attendance: Eligible")
elif 0 <= attendance < 75:
    print("Attendance: Not Eligible")
else:
    print("Attendance: Invalid")

if not (0 <= marks <= 100) or not (0 <= attendance <= 100):
    print("Final Result: Invalid Credentials")
elif marks >= 40 and attendance >= 75:
    print("Final Result: PASS")
else:
    print("Final Result: FAIL")