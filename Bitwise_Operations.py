#Number of trailing zeros

def trailZeros():
        var = int(raw_input("Enter a number: "))
        len_original = len(str(var))
        print len_original
        var_list = list(str(var))
        var_list.reverse()
        print var_list
        len_temp = len(str(int(''.join(var_list))))
        print len_temp
        return len_original - len_temp
        
        
        
         
