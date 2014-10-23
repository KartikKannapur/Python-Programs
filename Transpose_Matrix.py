#Transpose of a Matrix

def matrixTranspose():
        dim = int(raw_input("Enter the dimension of the matrix: "))
        array_input =[[0 for i in range(0,dim)]for j in range(0,dim)]
        array_output=[[0 for i in range(0,dim)]for j in range(0,dim)]

        for i in range(0,dim):
                for j in range(0,dim):
                        array_input[i][j] = int(raw_input("Enter an element:"))
        print array_input

        for i in range(0,dim):
                for j in range(0,dim):
                        array_output[i][j] = array_input[j][i]

        print array_output
