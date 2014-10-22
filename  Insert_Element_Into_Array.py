def insert_arr():
        length = int(raw_input("Enter the length of the array: "))
        arr = []

        for i in range(0,length):
                arr.append(int(raw_input("Enter an element in the array: ")))

        insert = int(raw_input("Enter at which position you would like to insert an element into the array"))
        ele = int(raw_input("Enter the element you would like to insert: "))
        arr.insert(insert,ele)

        return arr
        
