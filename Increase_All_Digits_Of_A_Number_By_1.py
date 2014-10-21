def inc_by_1(num):
        var = list(str(num))
        length = len(var)

        for i in range(0,length):
                var[i] = int(var[i])+ (1)
                
        var = str(var)
        res = "".join(map(str, var))
        return res
