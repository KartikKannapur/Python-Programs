string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
prefix = 'Hello'
suffix = 'World'

def sufpreWord():
        print "Word\t" + "Word Suffix\t" + "Word Prefix"
        for i in range(0,len(string)):
                print str(string[i])+"\t"+str(string[i])+str(suffix)+"\t"+str(prefix)+str(string[i])
        
