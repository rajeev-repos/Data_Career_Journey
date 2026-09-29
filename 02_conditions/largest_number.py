num1 = int(input("Enter your desired number: "))
num2 = int(input("Enter your desired number: "))
num3 = int(input("Enter your desired number: "))

if num1 > num2 and num1 > num3:
    print(num1," is the largest number")
elif num1 < num2 and num2 > num3:
    print(num2," is the largest number")
else:
    print(num3," is the largest number")
     