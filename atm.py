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
            # Step 6:While typing password, terminal does not display the pin
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
                clear = input('Please press "c" to clear screen ')
                if clear.lower() == 'c':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    time.sleep(2)
                print("=====THANK YOU FOR VISITNG BITS ATM=====")
                time.sleep(2)
                break
            elif choice == '2':
                amount = int(input("Enter amount to be deposited "))
                accountObj.deposit(amount)
                clear = input(' Please press "c" to clear screen')
                if clear.lower() == 'c':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    time.sleep(2)
                print("=====THANK YOU FOR VISITNG BITS ATM=====")
                time.sleep(2)
                break
            elif choice == '3':
                amount = int(input("Enter amount to be withdrawn "))
                accountObj.withdraw(amount)
                clear = input(' Please press "c" to clear screen')
                if clear.lower() == 'c':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    time.sleep(2)
                print("=====THANK YOU FOR VISITNG BITS ATM=====")
                time.sleep(2)
                break


atm = Atm()
atm.authorization()
