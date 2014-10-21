#An Armstrong number is an n-digit base b number such that the sum of its (base b) digits raised
#to the power n is the number itself
#1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153

def armstrong(num):
        length = len(str(num))
        var = list(str(num))
        sum = 0
        for i in range(0,length):
                sum = sum + int(var[i])**length
        if(sum == num):
                return sum

#for i in range(0,1000):
#        armstrong(i)
