def check_div_5(num1,num2):
        diff = num2 - num1
        if diff%5 == 0:
                var = (diff/5) - 1
        if diff == 5:
                var = 1
        else:
                var = (diff+5)/5
        print "Number of integers: " + str(var)
