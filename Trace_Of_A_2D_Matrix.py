#Trace of a Matrix
def traceOfMatrix():
        dim = int(raw_input("Enter the dimensions of the square matrix: "))
        matrix = [[0 for i in range(0,dim)]for j in range(0,dim)]

        for i in range(0,dim):
                for j in range(0,dim):
                        matrix[i][j] = int(raw_input("Enter an element in the matrix: "))

        trace = 0
        for i in range(0,dim):
                trace += matrix[i][i]

        return trace
