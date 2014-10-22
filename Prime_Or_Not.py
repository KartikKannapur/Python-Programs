import math

def isprime(num):
        for i in range(2,num):
                if(num%i == 0):
                        return "Not Prime"
                else:
                        return "Prime"
