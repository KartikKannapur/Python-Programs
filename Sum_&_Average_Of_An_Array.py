#Sum & Avg of an array
def sum_avg_arr(length):
        arr = []
        for i in range(0,length):
                arr.append(int(raw_input("Enter an element: ")))

        print arr
        print sum(arr)
        print (sum(arr)/length)
