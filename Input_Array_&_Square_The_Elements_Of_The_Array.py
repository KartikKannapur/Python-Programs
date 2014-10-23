def arraySquare():
        length = int(raw_input("Enter the length of the array: "))
        arr = []

        for i in range(0,length):
                arr.append(int(raw_input("Enter the element of an array: ")))
        print arr

        for i in range(0,length):
                arr[i] = arr[i]**2

        print arr
