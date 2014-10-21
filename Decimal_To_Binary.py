def dec_to_bin(num):
        arr =[]

        while num != 1:
                arr.append(num%2)
                num = num/2

        arr.append(1)
        arr.reverse()
        return arr
                
