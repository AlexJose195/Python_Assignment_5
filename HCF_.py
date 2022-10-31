# Write a Python Program to Find HCF.

print("\nFinding HCF of any two number\n")
First_number = int(input("Enter the first number : "))
Second_number = int(input("Enter the Second number : "))

for i in range(First_number, 0, -1):  # for finding the hcf of first number and second number.

    if First_number%i == 0 and Second_number%i==0: # if condition is true then i is the hcf.
        print("HCF of ", First_number, " and ", Second_number, " is : ",i)
        break

    else:
        continue
