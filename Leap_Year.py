def LeapYear(num):
        if((num%4 == 0) & (num%100 !=0)):
                return "Leap Year"
        if(num%400 ==0):
                return "Leap Year"
        else:
                return "Not a Leap Year"
