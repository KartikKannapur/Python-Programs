#Upper and Lower Triangular Matrix

def ultMat():
        dim = int(raw_input("Enter the dimension of the matrix: "))
        mat =[[0 for i in range(0,dim)]for j in range(0,dim)]

        for i in range(0,dim):
                for j in range(0,dim):
                        mat[i][j] = int(raw_input("Enter an element of the matrix"))

        upper_mat = []
        lower_mat = []
        for i in range(0,dim):
                for j in range(0,dim):
                        if(j>i):
                                upper_mat.append(mat[i][j])
                        if(j<i):
                                lower_mat.append(mat[i][j])

        print upper_mat,lower_mat
