'''list=[48,'Twelve','A building',32]
print(list[2])
for i in list:
    print(i)
for i in range(list):
    print(list[i])'''
#create a 2D list
'''matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(len(matrix))
print(matrix[1][1])
print(len(matrix[0]))
for i in range(len(matrix)):
    print('\n')
    for j in range(len(matrix[0])):
        print(matrix[i][j],end=' ')'''
#create a matrix by taking input
'''print('Pick the number of rows')
rows=int(input())
print('Pick the number of columns')
columns=int(input())
matrix=[]
for i in range(rows):
    temp=[]
    for j in range(columns):
        x=int(input('Enter the value(s)'))
        temp.append(x)
    matrix.append(temp)
print(matrix)'''
#add matrixes
'''matrixa=[[123,4895,32],[1243,48,2389],[8912,819024,240389]]
matrixb=[[456,78,785],[89,23,456],[45,563,89]]
result=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(3):
        result[i][j]=matrixa[i][j]+matrixb[i][j]
print(result)'''
#diagonal
square=[[5,6],[14,15]]
for i in range(2):
    print(square[i][i])