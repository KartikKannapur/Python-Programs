def permute(arr):
        print arr

        for i in range(0,len(arr)):
                temp = arr[0]
                arr[i] = arr[i+1]
                arr.append(temp)
        arr = arr[:5]
        print arr

        option = raw_input("Do you want to permute again? Y or N")
        if(option == 'Y'):
                permute(arr)
        else:
                print "Thank You"
        
def circular_permutation():
        length = int(raw_input("Enter the length of the array: "))
        arr = []

        for i in range(0,length):
                arr.append(int(raw_input("Enter an element of the array: ")))

        permute(arr)

circular_permutation()
