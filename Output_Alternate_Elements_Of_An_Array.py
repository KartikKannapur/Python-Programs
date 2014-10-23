def alternateArray():
        length = int(raw_input("Enter the length of the array: "))

        a =[]
        for i in range(0,length):
                a.append(int(raw_input("Enter the elements of the array: ")))
        for i in range(0,length,2):
                print a[i]
