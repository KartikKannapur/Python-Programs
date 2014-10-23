def repeated():
        arr = []
        length = int(raw_input("Enter the length of the array: "))

        for i in range(0,length):
                arr.append(int(raw_input("Enter the elements of an array: ")))
        arr.sort()
        count = 0
        for i in range(0,length):
                print "The number taken into consideration: " + str(i)
                print "The number of occurences of the number above: " + str(arr.count(i))
                        
