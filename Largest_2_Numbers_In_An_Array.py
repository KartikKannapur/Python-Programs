#Accept numbers via User Input to the Array
def large_arr(array):
        length = len(array)
        large = array[0]

        for i in range(0,length):
                if(array[i] > large):
                        large = array[i]
        print "Largest element :" + str(large)

        array.remove(large)

def main(length):
        arr = []
        for i in range(0,length):
                arr.append(int(raw_input("Enter an element: ")))
        
        large_arr(arr)
        large_arr(arr)
