#Fibonacci

def fibo(n):
        add = 0
        if(n == 1):
                return add + 1
        if(n == 2):
                return add + 1
        if(n == 3):
                return add + 2

        if(n>3):
                return (fibo(n-1) + fibo(n-2))
