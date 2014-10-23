#Check for Identity
def identity():

        dim = int(raw_input("Enter the dimensions of the matrices: "))

        mat = [[0 for i in range(0,dim)]for j in range(0,dim)]
        
        for i in range(0,dim):
                for j in range(0,dim):
                        mat[i][j] = int(raw_input("Enter an element in the matrix: "))
                        
        count = 0
        for i in range(0,dim):
                for j in range(0,dim):
                        if ((i == j) & (mat[i][j] == 1)):
                                count +=1
                        if((i != j) & (mat[i][j] == 0)):
                                count += 1
                                

        if(count == 9):
                return "Identity"
        else:
                return "Noooo"
