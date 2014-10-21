def sum_of_digits(num):
        sum = 0
        digits = len(str(num))

        for i in range(0,digits):
                var = num % 10
                sum = sum + var
                num = num/10

        return sum
