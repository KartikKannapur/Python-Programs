#Equality of 2 Matrices

def equMat():

        dim = int(raw_input("Enter the dimensions of the matrices: "))

        mat1 = [[0 for i in range(0,dim)]for j in range(0,dim)]
        mat2 = [[0 for i in range(0,dim)]for j in range(0,dim)]

        for i in range(0,dim):
                for j in range(0,dim):
                        mat1[i][j] = int(raw_input("Enter an element in the matrix: "))

        for i in range(0,dim):
                for j in range(0,dim):
                        mat2[i][j] = int(raw_input("Enter an element in the matrix: "))

        print mat1
        print mat2

        count = 0
        for i in range(0,dim):
                for j in range(0,dim):
                        if(mat1[i][j] == mat2[i][j]):
                                count += 1

        if(count == 9):
                return "Equal"
        else:
                return "Unequal"
                
