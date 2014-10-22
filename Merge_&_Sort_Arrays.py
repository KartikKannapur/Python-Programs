def mergeAndSort():
        arr_1 = []
        arr_2 = []

        length_1 = int(raw_input("Enter the length of the first array: "))
        length_2 = int(raw_input("Enter the length of the second array: "))

        for i in range(0,length_1):
                arr_1.append(int(raw_input("Enter an element in an array: ")))

        for i in range(0,length_2):
                arr_2.append(int(raw_input("Enter an element in an array: ")))

        arr = arr_1 + arr_2
        arr.sort()

        return arr
        
                
