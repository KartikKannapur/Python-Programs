#Count the number of zeros and fives in a number
def countZeroFive(n):
        count = 0
        occur = 0
        var = str(n)
        while(count<len(var)):
                if(var[count] == '0' or var[count] == '5'):
                        occur = occur + 1
                count = count + 1
        return occur
