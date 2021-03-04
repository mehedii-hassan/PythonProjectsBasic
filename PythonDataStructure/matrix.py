matrix=[
    [1,2,3],
    [3,5,6],

]
matrix[0][2]=10    #matrix value change --------
#printing matrix using nested for loop--------------
for row in matrix:
    for col in row:
        print(col,end=" ")
    print()