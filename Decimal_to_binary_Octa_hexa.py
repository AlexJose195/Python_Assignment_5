#  Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal.

print("\nConverting Decimal to Binary , Octal and Hexadecimal.\n")
n = int(input("Enter any number : "))
print("")

b = n # for binary
o = n # for Octal
h = n # for hexadecimal

""" n is assigned to different value becuase n will be changed in run time and we 
have to convert n in three different numeral system."""

string_binary = ''
string_octal = ''
string_hexadecimal = ''

"""Different string are define for storing the remainder."""

# Decimal to Binary

while(True):

    remainder = b%2
    quotient  = b//2
    b=quotient
    string_binary = string_binary + str(remainder)
    if quotient < 2:
        string_binary = string_binary + str(quotient)
        print("Decimal to Binary :",n, "  = " ,int(string_binary[::-1]))
        break
    else :
        continue

# Decimal to Octal

while(True):
    remainder = o%8
    quotient  = o//8
    b=quotient
    string_octal = string_octal + str(remainder)
    if quotient < 8:
        string_octal = string_octal + str(quotient)
        print("Decimal to Octal :",n, "  = " ,int(string_octal[::-1]))
        break
    else :
        continue

# Decimal to Hexadecimal

while(True):
    remainder = o%16
    quotient  = o//16
    b=quotient
    string_hexadecimal = string_hexadecimal + str(remainder)
    if quotient < 16:
        string_hexadecimal = string_hexadecimal + str(quotient)
        print("Decimal to Hexadecimal :",n, "  = " ,int(string_hexadecimal[::-1]))
        break
    else :
        continue


