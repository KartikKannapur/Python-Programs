#LCM

def factors(n):
        arr = []
        for i in range(1,n+1):
                if(n % i == 0):
                        arr.append(i)
        return arr

def lcm(a,b):
        num_a = factors(a)
        num_b = factors(b)
        set_ab = set(num_a) & set(num_b)
        list_ab = list(set_ab)
        hcf = list_ab[len(list_ab)-1]

        prod = set(num_a) & set(num_b)
        prod = list(prod)
        print prod
        
        return((a*b)/hcf)
        
        
        
