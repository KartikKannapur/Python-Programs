#Perfect Number
#6 = 1 + 2 + 3

def perfect(num):
        sum =0
        for i in range(1,num):
                if(num%i == 0):
                        sum = sum + i
        if(sum == num):
                return "It is a perfect number"
        else:
                return "It is not a perfect number"
