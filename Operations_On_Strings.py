#Operations on Strings

def checkPalindrome():
        string = raw_input("Enter a string")
        if(string == string[::-1]):
                return "It is a Palindrome"
        else:
                return "It is not a Palindrome"

def readConcatenate():
        str1 = raw_input("Enter a string: ")
        str2 = raw_input("Enter the second string: ")
        print str1
        print str2
        print (str1 + str2)
def countVowCons():
        string = raw_input("Enter a string: ")
        string_lower = string.lower()
        
        count = 0
        for i in range(0,len(string_lower)):
                if(string_lower[i] == 'a'):
                        count += 1
                if(string_lower[i] == 'e'):
                        count += 1
                if(string_lower[i] == 'i'):
                        count += 1
                if(string_lower[i] == 'o'):
                        count += 1
                if(string_lower[i] == 'u'):
                        count += 1
        print "The number of Vowels are: " + str(count)
        print "The number of Consonants are: "+ str(len(string_lower)-count)

def substringInString():
        string = raw_input("Enter a string: ")
        sub_string = raw_input("Enter a substring: ")

        var = string.find(sub_string)
        if(var != (-1)):
                print "Successful"
        else:
                print ":( Unsuccessful"
                
def sumNumbersString():
        string = raw_input("Enter a string: ")
        sum = 0
        for i in range(0,len(string)):
                if(string[i].isdigit() == True):
                       sum = sum + int(string[i])

        return sum
