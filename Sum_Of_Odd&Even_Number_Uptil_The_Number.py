def OddEvenSum(num):
        sum_even = 0
        sum_odd =0
        for i in range(1,num+1):
                if i%2 == 0:
                        sum_even = sum_even + i
                if i%2 == 1:
                        sum_odd = sum_odd + i
        print "Even Sum:" + str(sum_even)
        print  "Odd Sum:" + str(sum_odd)
