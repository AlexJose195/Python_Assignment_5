# Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations.

print("\n Basic Calculator \n")
a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))

c = int(input("Enter your choice : \n1 - Addition. \n2 - Subtraction. \n3 - Multiplication \n4 - Division.\n "))

if c == 1:
    print("The Addition of ",a," and ",b, "is : ",a+b)

elif c == 2:
    print("The Subtraction of ",a," and ",b, "is : ",a-b)

elif c == 3:
    print("The Multiplication of ",a," and ",b, "is : ",a*b)

elif c == 4:

    if b == 0:
        print("Any number divided by '0' is not define or infinite.")

    else:
        print(a,"Divide by",b, "is : ",a/b)

else:
    print("Please, enter number between 1 to 4.")