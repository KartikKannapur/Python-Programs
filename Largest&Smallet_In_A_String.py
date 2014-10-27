#Largest and Smallest Word in a String
def largeSmall():
        string = raw_input("Enter a string: ")

        arr = []
        arr = string.split(" ")
        count= []

        for i in range(0,len(arr)):
                count.append(len(arr[i]))
        for i in range(0,len(count)):
                large = 0
                small = count[0]
                if(count[i] > large):
                        large = count[i]
                if(count[i] < small):
                        small = count[i]
        print small,large
        
