#Number of bits
i = 0
def findBits():
        num = int(raw_input("Enter a number: "))
        i = 1
        while(2**i) < num:
                i = i+1
        return i-1

#Replacing custom bits
def repCustomBits():
        a = raw_input("Enter a string: ")
        i = int(raw_input("Enter the first instance of the number: "))
        j = int(raw_input("Enter the second instance of the number: "))
        temp = a[i]
        a.replace(a[i],a[j])
        a.replace(a[j],temp)
        return a

#Check for power of 2
def powOfTwo(num):
        findBits()
        print i
        return (num%2**(i+1))
        
