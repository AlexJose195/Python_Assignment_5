# Write a Python Program to Find LCM.

print("\nFinding LCM of any two number\n")
First_number = int(input("Enter the first number : "))
Second_number = int(input("Enter the Second number : "))

for i in range(First_number, 0, -1):  # for finding the hcf of first number and second number.

    if First_number % i == 0 and Second_number % i == 0:  # if condition is true then i is the hcf.

        lcm = (First_number * Second_number) / i  # Mutliplication of two number is equal to the product of its hcf and lcm.
        print("LCM of ", First_number, " and ", Second_number, " is : ", lcm)
        break

    else:
        continue


