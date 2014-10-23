#Product of 2 Matrices

def productMatrix():
        dim = int(raw_input("Enter the dimension of both the matrices: "))

        mat1 =[[0 for i in range(0,dim)]for j in range(0,dim)]
        mat2 = [[0 for i in range(0,dim)]for j in range(0,dim)]

        for i in range(0,dim):
                for j in range(0,dim):
                        mat1[i][j] = int(raw_input("Enter an element: "))
        print mat1

        for i in range(0,dim):
                for j in range(0,dim):
                        mat2[i][j] = int(raw_input("Enter an element: "))
        print mat2

        mat_output = [[0 for i in range(0,dim)]for j in range(0,dim)]

        for i in range(0,dim):
                for j in range(0,dim):
                        count = 0
                        while(count < 3):
                                mat_output[i][j] += mat1[i][count]*mat2[count][j]
                                count += 1
        print mat_output
