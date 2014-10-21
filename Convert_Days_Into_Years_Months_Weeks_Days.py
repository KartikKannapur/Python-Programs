def year_conv(num):
        #num = number of days
        year = num/365
        rem_days = num%365
        week = rem_days/7
        rem_days = rem_days%7
        return str(year)+"years "+str(week)+"weeks "+str(rem_days)+"days"
