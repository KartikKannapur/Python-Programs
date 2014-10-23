def countOddEven():
        arr =[]
        length = int(raw_input("Enter  the number of elements in the array: "))

        for i in range(0,length):
                arr.append(int(raw_input("Enter an element in the array")))

        count_odd = 0
        count_even = 0
        for i in range(0,length):
                if(arr[i]%2 == 0):
                        count_even += 1
                if(arr[i]%2 ==1):
                        count_odd += 1
                else:
                        print "Error"

        print count_even,count_odd
