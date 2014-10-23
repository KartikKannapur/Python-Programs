#Addition or Subtraction of 2 Matrices

def addSubMat():
        dim = int(raw_input("Enter the dimensions of the 2 matrices: "))
        mat_1 = [[0 for i in range(0,dim)]for j in range(0,dim)]
        mat_2 = [[0 for i in range(0,dim)]for j in range(0,dim)]

        for i in range(0,dim):
                for j in range(0,dim):
                        mat_1[i][j] = int(raw_input("Enter an element: "))
        print mat_1

        for i in range(0,dim):
                for j in range(0,dim):
                        mat_2[i][j] = int(raw_input("Enter an element: "))
        print mat_2

        array_sum = [[0 for i in range(0,dim)]for i in range(0,dim)]
        array_diff = [[0 for i in range(0,dim)]for i in range(0,dim)]
        
        for i in range(0,dim):
                for j in range(0,dim):
                        array_sum[i][j] = mat_1[i][j] + mat_2[i][j]
                        array_diff[i][j] = mat_1[i][j] - mat_2[i][j]

        print array_sum,array_diff
