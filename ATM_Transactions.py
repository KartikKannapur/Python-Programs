def main():
        print "*****Welcome to your ATM*****"
        pswd = int(raw_input("Enter your PIN:"))

        #Pre-Set ATM pin to 9999
        if(pswd == 9999):
                print "*****Your PIN is verified and is correct*****"
                option = int(raw_input("Please select an option:\n1.Check your balance\n2.Withdraw money\n3.Deposit money\n4.Quit\n"))
                if(option == 1):
                        print "*****You have chosen Option 1: To check your balance*****"
                        print "*****Balance: "+str(1000)+"*****"
                if(option == 2):
                        print "*****You have chosen Option2: Withdraw money*****"
                        withdraw_amt = int(raw_input("Enter the amount you would like to withdraw: "))
                        print "*****You have withdrawn an amount of: Rs."+str(withdraw_amt)+"*****"
                        print "*****Remaning balance is: Rs."+str(1000 - withdraw_amt)+"*****"
                if(option == 3):
                        print "*****You have chosen Option3: Deposit money*****"
                        deposit_amt = int(raw_input("Enter the amount you would like to deposit: "))
                        print "*****You have deposited an amount of: Rs."+str(deposit_amt)+"*****"
                        print "*****Remaning balance is: Rs."+str(1000 + deposit_amt)+"*****"
                if(option == 4):
                        print "*****You have chosen Option4: Quit*****"
                
                print "*****Thank you for banking with us*****"
                 
        else:
                print "*****Please re-enter your PIN*****"
                main()
