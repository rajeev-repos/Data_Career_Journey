marks=int(input("Enter your marks: "))


if marks<=100 and marks>=80:
    print("Distinction")
elif marks <80 and marks>=60:
    print("First Division")
elif marks<60 and marks>=40:
    print("Pass")
elif marks<40 and marks>=0:
    print("Fail")
else:
    print("Invalid Marks")