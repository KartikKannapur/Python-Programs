def arraySquare():
        row = int(raw_input("Enter the row size: "))
        column = int(raw_input("Enter the column size: "))

        arr = [[0 for i in range(0,column)]for i in range(0,row)]
        #Initialize the multi dimensional array
        for i in range(0,row):
                for j in range(0,column):
                        arr[i][j] = int(raw_input("Enter an element to the array: "))
        print arr

        for i in range(0,row):
                for j in range(0,column):
                        arr[i][j] = arr[i][j]**2
        print arr
