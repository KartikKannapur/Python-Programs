def count_ones(num):
        var = list(str(num))
        count = 0

        for i in range(0,len(var)):
                if(var[i] == '1'):
                        count = count + 1
        return count
