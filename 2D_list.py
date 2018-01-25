m = int(input("Enter the number of row"))
n=int(input("Enter the number of the coloumn"))
multi_list=[[0 for col in range(n)]for row in range(m)]#initilize the list
for i in range(m):
    for j in range(n):
        multi_list[i][j] = i*j;
print(multi_list)
