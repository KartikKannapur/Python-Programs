#Frequency of ODD & EVEN Numbers in a matrix
def oddEven():

        dim = int(raw_input("Enter the dimensions of the matrices: "))

        mat = [[0 for i in range(0,dim)]for j in range(0,dim)]
        for i in range(0,dim):
                for j in range(0,dim):
                        mat[i][j] = int(raw_input("Enter an element in the matrix: "))

        print mat
        
        even_count =0
        odd_count = 0
        for i in range(0,dim):
                for j in range(0,dim):
                        if(mat[i][j] % 2 == 0):
                                even_count += 1
                        else:
                                odd_count += 1
        print "Frequency of ODD & EVEN:" + str(odd_count) + str(even_count)
