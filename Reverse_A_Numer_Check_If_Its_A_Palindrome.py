def reverse_pali(num,num_again,digits):
        arr = []
        brr = []
        for i in range(0,digits):
                arr.append(num%10)
                num =  num/10
        print arr
        arr.reverse()
        print arr

        for i in range(0,digits):
                brr.append(num_again%10)
                num_again =  num_again/10
        print brr
        
        if brr == arr:
                print "It is a Palindrome"
        else:
                print "It is not a Palindrome"
