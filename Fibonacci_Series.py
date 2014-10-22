#Generate a Palindrome
def palindrome(digits):
        var_1 = 1
        var_2 = 1
        var_3 = 2
        count = 2
        sum = 2
        var = var_2
        print 1
        total = 1
        while(count <= digits):
                count += 1
                print total
                total = sum + var
                var = sum
                sum = total
