grid= [[],[],[],[],[]]
for i in range(0,5):
    for j in range(0,5):
        grid[i].append(0)
input1 = input("Enter a row num from 1 to 5: ")
input2 = input("Enter a col num from 1 to 5: ")
grid[int(input1)-1][int(input2)-1]=1
for i in range(0,5):
    print(grid[i])