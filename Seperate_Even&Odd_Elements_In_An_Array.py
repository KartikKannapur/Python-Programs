def even_odd_arr(length):
        arr = []
        arr_even = []
        arr_odd = []
        for i in range(0,length):
                arr.append(int(raw_input("Please enter an element: ")))

        for i in range(0,length):
                if(arr[i]%2 == 0):
                        arr_even.append(arr[i])
                else:
                        arr_odd.append(arr[i])

        print arr_even
        print arr_odd
