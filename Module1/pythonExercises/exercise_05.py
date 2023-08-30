List1 = []
List2 = []
for i in range(1,6):
    intInput = int(input("Enter a number for the first list: "))
    List1.append(intInput)
for i in range(1,6):
    intInput = int(input("Enter a number for the second list: "))
    List2.append(intInput)
print("First List: "+str(List1))
print("Second List: "+str(List2))
print("Common List: "+str(list(set(List1).intersection(List2))))