listNumber = []
TotalNumber = 0
print("Enter a number: ")
intInput = int(input())
for i in range(1,intInput+1):
    print("Enter number "+str(i)+": ")
    intInput2 = int(input())
    listNumber.append(intInput2)
    TotalNumber = TotalNumber + intInput2
print("List: "+str(listNumber))
print("Average: "+str(TotalNumber/intInput))