inputList = []
for i in range(5):
    userInput= input("Enter a word: ")
    inputList.append(userInput)
inputListStr = ""
for i in range(5):
    inputListStr=inputListStr +" "+inputList[i]
print("Words: "+str(inputList))
print("One String: "+inputListStr)