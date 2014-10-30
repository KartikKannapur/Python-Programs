#PRIME - Faster

import math

def prime(n):
        val = math.ceil(math.sqrt(n))
        for i in range(2,int(val)):
                if(n % i) == 0:
                        return "Not Prime"
                else:
                        return "Prime"
