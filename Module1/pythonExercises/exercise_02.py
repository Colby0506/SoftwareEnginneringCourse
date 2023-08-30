print("Enter a string: ")
string1 = input()
print("Enter another string: ")
string2 = input()
if string1 in string2:
    print(True)
elif string2 in string1:
    print(True)
else: 
    print(False)