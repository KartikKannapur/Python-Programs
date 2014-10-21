def sum_digits(num):
        sum = 0
        for i in range(0,len(str(num))):
                sum += (num%10)
                num /= 10
        return sum
