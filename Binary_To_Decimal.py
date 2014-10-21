def bin_to_dec(num,digits):
        sum = 0
        m = 1
        for i in range(0,digits):
                var = num%10
                sum = sum + var*m
                m = m*2
                num = num/10
        print sum
        
