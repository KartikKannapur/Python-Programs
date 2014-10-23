#To convert a string into ASCII Value -> ord()

def convertToASCII():
        st = raw_input("Enter a string: ")
        st_arr = list(st)
        arr = []

        for i in range(0,len(st_arr)):
                arr.append(ord(st_arr[i]))

        return arr
