UserInput = input("Enter a string: ")
UserInputList = list(UserInput)
FinalList = []
TempList = []
count =0
for i in range(len(UserInputList)):
    if count ==3:
        FinalList.append(TempList)
        TempList=[]
        count=0
    TempList.append(UserInputList[0])
    UserInputList.pop(0)
    count = count +1
FinalList.append(TempList)
print(FinalList)