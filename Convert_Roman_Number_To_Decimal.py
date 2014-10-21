def roman_to_dec(rom_num):
        #I = 1
        #V = 5
        #X = 10
        #L = 50
        #C = 100
        #D = 500
        #M = 1,000

        sum = 0
        arr = list(rom_num)
        length = len(list(rom_num))
        for i in range(0,length):
                var = arr[i]
                if var == 'I':
                        sum = sum + 1
                if var == 'V':
                        sum = sum + 5
                if var == 'X':
                        sum = sum + 10
                if var == 'L':
                        sum = sum + 50
                if var == 'C':
                        sum = sum + 100
                if var == 'D':
                        sum = sum + 500
                if var == 'M':
                        sum = sum + 1000

        return sum
#Exceptions :  IX = 9, XC = 90, and CM = 900
                        
