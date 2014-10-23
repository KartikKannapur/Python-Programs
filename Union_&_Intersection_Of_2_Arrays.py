#Union and Intersection

def union_inter():
        length_1 = int(raw_input("Enter the length of the first array: "))
        length_2 = int(raw_input("Enter the length of the second array: "))
        arr_1 = []
        arr_2 =[]

        for i in range(0,length_1):
                arr_1.append(int(raw_input("Enter an element in the array: ")))
        print "The first array that you have entered is: " + str(arr_1)

        for i in range(0,length_2):
                arr_2.append(int(raw_input("Enter an element in the array: ")))
        print "The second array that you have entered is: " + str(arr_2)

        arr_union = []
        arr_intersection = []
        for i in range(0,length_1):
                for j in range(0,length_2):
                        if(arr_1[i] == arr_2[j]):
                                arr_intersection.append(arr_1[i])
                        else:
                                arr_union.append(arr_1[i])
                                arr_union.append(arr_2[j])

        removeDuplicate(arr_union)
        removeDuplicate(arr_intersection)

        return arr_union,arr_intersection

def removeDuplicate(array):
        length = len(array)
                
        for i in range(1,length):
                if(array[i] == array[i-1]):
                        array.remove(array[i])
        return array
