from account import Account
from getpass import getpass


class Atm:

    def authorization(self):
        while True:
            #Step 1:Clear the screen
            #Step 2:Print Welcome message
            #Step 3: Ask for account number
            #Step 4:Ask for pin
            #Step 5:Verify and print yes or no if pin is correct or not
            #Step 6: While typing password, terminal should display ****
            print("Welcome to my atm")
            while True:
                accountObj = Account()
                inputAccountNumber=input("enter account id ")
                searchResult = accountObj.searchAccountId(inputAccountNumber)

                if len(searchResult)==1:
                    
                    accountObj.accountHolderName = searchResult[0]['accountHolderName']
                    accountObj.accountId=searchResult[0]['accountId']
                    accountObj.balance=searchResult[0]['balance']
                    accountObj.pin=searchResult[0]['pin']

                    count=0
                    while(count<3):
                        print("Enter account pin ")
                        pin = getpass()
                        if pin == accountObj.pin:
                            print("Authenticated")
                            self.performAccountInteractions(accountObj)

                            break
                        else:
                            if(count!=2):
                                print("Bad Pin.Try again")
                            count+=1
                        if(count==3):
                            print("User not authenticted")
                        continue
                else:
                    print("Not Found")
                    continue
        
    def printAtmMenu(self):
        #Print Menu
        print("======WELCOME TO BITS ATM======")
        print("Select your transaction.")
        print("Press 1 to view balance.")
        print("Press 2 to deposit")
        print("Press 3 to withdraw")
        
    def performAccountInteractions(self, accountObj):
        while True:
            self.printAtmMenu()
            choice=input()
            print("user choice ", choice)
            if choice=='1':
                accountObj.showBalance()
            elif choice=='2':
                amount=int(input("Enter amount to be deposited "))
                accountObj.deposit(amount)
            elif choice=='3':
                amount=int(input("Enter amount to be withdrawn "))
                accountObj.withdraw(amount)
            elif choice=='4':
                print("=====THANK YOU FOR VISITING BITS ATM=====")
                break


atm = Atm()
atm.authorization()
#figure out requirements.txt and add it to your repo
#commit all files except .json to github
#learn about gitIgnore file(to ignore __pycache__)

