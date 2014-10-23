#Sum of elements in each row and column

def rowColSum():
        dim = int(raw_input("Enter the dimension of the matrix: "))
        mat = [[0 for i in range(0,dim)]for j in range(0,dim)]

        for i in range(0,dim):
                for j in range(0,dim):
                        mat[i][j] = int(raw_input("Enter an element in the matrix: "))

        print "The matrix entered is: " +str(mat)

        row_sum = []
        col_sum = []
        for i in range(0,dim):
                Rsum = 0
                Csum = 0
                for j in range(0,dim):
                        Rsum += mat[i][j]
                        Csum += mat[j][i]
                row_sum.append(Rsum)
                col_sum.append(Csum)

        print row_sum,col_sum
