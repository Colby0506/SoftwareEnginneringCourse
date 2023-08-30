inputList = []
while True:
    inputUser = input("Enter a number or QUIT to quit: ")
    if inputUser == "QUIT":
        break
    inputList.append(int(inputUser))
print("All Nums: " +str(inputList))
evenList = []
for i in range(len(inputList)-1):
    if (inputList[i]%2)==0:
        evenList.append(inputList[i])
print("Even nums: "+str(evenList))