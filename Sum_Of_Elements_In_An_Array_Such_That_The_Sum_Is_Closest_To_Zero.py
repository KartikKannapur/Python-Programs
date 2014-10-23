#Sum of 2 elements in the 
def sumClosestToZero() :
        length = int(raw_input("Enter the length of the array: "))
        arr = []

        for i in range(0,length):
                arr.append(int(raw_input("Enter an element in thearray: ")))
        print arr

        sumZero = []
        for i in range(0,length):
                for j in range(0,length):
                        if(arr[i] != arr[j]):
                                sumZero.append(arr[i]+arr[j])
                                print sumZero
        sumZero.sort()

        arr_neg = []
        arr_pos = []
        for i in range(0,length):
                if(arr[i] ==  0):
                        print arr[i]
                if(arr[i] < 0):
                        arr_neg.append(arr[i])
                if(arr[i] > 0):
                        arr_pos.append(arr[i])
        arr_merge = arr_pos + arr_neg
        arr_merge.sort()
        print arr_merge[0]
