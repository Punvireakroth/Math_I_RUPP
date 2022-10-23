import numpy as np

def zero_matrix(rows, cols):
    "Creates a zero matrix of size `rows` and `cols`."
    
    A = []
    
    for i in range(rows):
        A.append([])
        for j in range(cols):
            A[-1].append(0.0)
            
    return A

def copyMatrix(M):
    "Create copies of the given matrix."
    
    row = len(M)
    col = len(M[0])
    
    MC = zero_matrix(row, col)
    
    for i in range(row):
        for j in range(col):
            MC[i][j] = M[i][j]
            
    return MC

def inverseMatrix(x):
    
    
    if len(x) == len(x[0]):
        if np.linalg.det(x) != 0:
            A_copy = copyMatrix(x)
            I = np.identity(len(x))
            I_copy = copyMatrix(I)
            
            indices = list(range(len(x)))
            
            for fd in range(len(x)):
                fdScaler = 1.0 / A_copy[fd][fd]
                
                for j in range(len(x)):
                    A_copy[fd][j] *= fdScaler
                    I_copy[fd][j] *= fdScaler
                    
                for i in indices[0:fd] + indices[fd+1:]:
                    crScaler = A_copy[i][fd]
                    
                    for j in range(len(x)):
                        A_copy[i][j] = A_copy[i][j] - crScaler * A_copy[fd][j]
                        I_copy[i][j] = I_copy[i][j] - crScaler * I_copy[fd][j]
                        
            print("Your matrix is:")
            for row in x:
                print([round(x,3)+0 for x in row])
            print("-----------------------------")
            print("The inverse of your matrix is:")
            for row in I_copy:
                print([round(x,3)+0 for x in row])
        else:
            print("Cannot find inverse matrix is 0")
    else:
        print("Cannot find inverse matrix becuase it is not square matrix")


inverseMatrix([[1,2,-1], [2, 5, 1],[-1,-2,2]])