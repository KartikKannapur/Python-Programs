def octal_2_bin(num):
        var = list(str(num))
        length=len(var)

        for i in range(0,length):
                bin(int(var[i]))
