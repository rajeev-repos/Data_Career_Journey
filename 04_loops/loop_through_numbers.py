marks = [75, 82, 68, 91, 56]

for mark in marks:
    print(mark)

for mark in marks:
    if mark >= 80:
        print(mark, "Distinction")
    elif mark >= 60:
        print(mark, "First Division")
    else:
        print(mark, "Pass")