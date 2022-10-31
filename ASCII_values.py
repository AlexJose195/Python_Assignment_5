# Write a Python Program To Find ASCII value of a character.

print("\nFinding ASCII value of a character")
enter_string = input("\nEnter The string : ")
for char in enter_string:
    print(char," ASCII value is :",ord(char))