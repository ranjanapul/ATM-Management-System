from account import Account
import time
from card import Card
from user import User
import os


class Atm:

    def authorization(self):
        while True:
            # Step 1:Clear the screen
            # Step 2:Print Welcome message
            # Step 3: Ask for account number
            # Step 4:Ask for pin
            # Step 5:Verify and print yes or no if pin is correct or not
            # Step 6: While typing password, terminal should display ****
            print("Welcome to my atm")
            while True:
                cardObj = Card()
                isAuthenticated = cardObj.authenticateCardPin()
                if isAuthenticated is False:
                    continue

                userObj = User()
                userObj.card = cardObj
                accountId = userObj.getAccountId()
                if accountId is False:
                    continue
                accountObj = Account()
                accountInformation = accountObj.searchAccountId(accountId)
                accountObj.accountHolderName =\
                    accountInformation[0]['accountHolderName']
                accountObj.accountId = accountInformation[0]['accountId']
                accountObj.balance = accountInformation[0]['balance']
                self.performAccountInteractions(accountObj)

    def printAtmMenu(self):
        print(" ======WELCOME TO BITS ATM======")
        print("Select your transaction.")
        print("Press 1 to view balance.")
        print("Press 2 to deposit")
        print("Press 3 to withdraw")

    def performAccountInteractions(self, accountObj):
        while True:
            self.printAtmMenu()
            choice = input()
            print("user choice ", choice)
            if choice == '1':
                accountObj.showBalance()
            elif choice == '2':
                amount = int(input("Enter amount to be deposited "))
                accountObj.deposit(amount)
            elif choice == '3':
                amount = int(input("Enter amount to be withdrawn "))
                accountObj.withdraw(amount)
            elif choice == '4':
                print("=====THANK YOU FOR VISITING BITS ATM=====")
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                break


atm = Atm()
atm.authorization()
# figure out requirements.txt and add it to your repo
#  Write a readme file. List:
# 1)How to run the program.
# 2)What are the package dependencies like tinydb,getpass
# 3)What is tiny db and why did we use it?
# 4)What attributes are saved in database
# 5) Description of each file
# 6) List of key features
# 7)Future extensions: Hashing of pincodes

'''
ToDo:
1) Dont ask account number. Ask card number
2)Verify pincode
3)If verified ask User class about card kis user ka hai aur uska acc no kya hai
4)Once account no. is received, then all transactions etc.
'''
