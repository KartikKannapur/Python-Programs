#More Operations on Strings

def findCapital():
        string = raw_input("Enter a string with a capital letter: ")
        for i in range(0,len(string)):
                if(string[i] < "a") and (string[i] >="A"):
                        return string[i]

def anagramChecker() :
        string1 = raw_input("Enter the first string :")
        string2 = raw_input("Enter the second string: ")
        print string1,string2
        string1 = list(string1)
        string2 = list(string2)

        string1.sort()
        string2.sort()
        print string1,string2

        if(string1 == string2):
                return "ANAGRAM :)"

def removeString():
        string = raw_input("Enter a string:")
        string_remove =raw_input("Enter the string that you want to remove: ")

        string = list(string)
        strgin_remove = list(string_remove)

        for i in range(0,len(string_remove)):
                string.remove(string_remove[i])

        arr =[]
        for i in range(0,len(string)):
                arr.append(string[i])
        print arr

def comboString():
        string = raw_input("Enter a string: ")

        for j in range(0,len(string)):
                print(string[j:len(string)])
                print(string[j:len(string)][::-1])
                        
def LongestRepeatingSequence():
        sqnce = raw_input("Enter a sequence: ")


        
