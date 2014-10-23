#Find the largest sub-array of Numbers

def subArraySum() :
        length = int(raw_input("Enter the length of the array: "))
        arr = []

        for i in range(0,length):
                arr.append(int(raw_input("Enter an element in thearray: ")))
        print arr

        large = 0
        for i in range(0,length+1):
                for j in range(0,length+1):
                        if sum(arr[i:j]) > large:
                                large = sum(arr[i:j])

        print large
