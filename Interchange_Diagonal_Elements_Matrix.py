#Program to accept a Matrix and Interchange the diagonals

def acceptInterchange():
        dim = int(raw_input("Enter the dimension of the matrix: "))
        mat =[[0 for i in range(0,dim)]for j in range(0,dim)]

        for i in range(0,dim):
                for j in range(0,dim):
                        mat[i][j] = int(raw_input("Enter an element of the matrix"))

        array = [[0 for i in range(0,dim)]for j in range(0,dim)]
        for i in range(0,dim):
                        array[i][i] = mat[i][(dim-1)-i]
        print array
        print mat
