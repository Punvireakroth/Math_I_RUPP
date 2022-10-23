import numpy as np

def gaussElimination(matrix):
    np.asarray(matrix) 
    matrix = matrix.astype(float)
    print ("the initial matrix:")
    print (matrix)
    if matrix[0,0] == 0.0:
        raise Exception("matrix row 1 column 1 cannot be zero!")
    n,m = matrix.shape
    print ("row:",n,"column:",m)
    for i in range(0,n):#row
        for j in range(i+1,n):
            if matrix[j,i] != 0.0:
                print ("using row ",i,"as pivot and row ",j,"as target")
                multiplier = matrix[j,i]/matrix[i,i]
              
                matrix[j,i:m]=matrix[j,i:m] - multiplier*matrix[i,i:m] 
                print (matrix)

    x = []
    substractor = 0.0
    for i in range(n-1,-1,-1): #row
      
        for j in range(0,n-i): #column
            
            if j==0:
                substractor = 0
            else:
                substractor = substractor + matrix[i,m-j-1]*x[j-1]
        x.append((matrix[i,m-1]-substractor)/matrix[i,i])
      
    return x



a = np.array([[2,1,-3],
             [1,-1,2],
             [7,-2,3]]
)
result = gaussElimination(a)
print ("the result is" ,result)