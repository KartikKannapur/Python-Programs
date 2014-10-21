def read_and_describe():
        grade = raw_input("Enter the grade: ")

        if(grade == 'S'):
                return "Super"
        if(grade == 'A'):
                return "Average"
        if(grade == 'F'):
                return "Fail"
        if(grade == 'DNW'):
                return "Did not write"
        else:
                return read_and_describe()
        
        
