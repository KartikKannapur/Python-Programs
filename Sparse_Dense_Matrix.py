#Determine if the matrix is a Sparse Matrix or a Dense Matrix

def sparseDense():
        dim = int(raw_input("Enter the dimension of the matrix: "))
        mat =[[0 for i in range(0,dim)]for j in range(0,dim)]

        for i in range(0,dim):
                for j in range(0,dim):
                        mat[i][j] = int(raw_input("Enter an element of the matrix"))

        count_zero = 0
        count_non_zero = 0
        for i in range(0,dim):
                for j in range(0,dim):
                        if(mat[i][j] == 0):
                                count_zero += 1
                        if(mat[i][j] != 0):
                                count_non_zero += 1

        if(count_zero > count_non_zero):
                return "Sparse"
        if(count_non_zero > count_zero):
                return "Dense"
