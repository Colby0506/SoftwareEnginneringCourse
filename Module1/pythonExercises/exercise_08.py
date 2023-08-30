inputList = []
for i in range(1,11):
    userInput = input("Enter number "+str(i)+": ")
    inputList.append(int(userInput))
print("Original List: "+str(inputList))
listFinal = (list(set(inputList)))
for i in range(len(listFinal)-1):
    if inputList.count(listFinal[i])>1:
        listFinal.remove(listFinal[i])
print("Nums that appear once: "+str(listFinal))