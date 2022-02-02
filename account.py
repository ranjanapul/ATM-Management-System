from tinydb import TinyDB, Query

class Account:

    def __init__(self):

        print("Construct New Object")

        self.accountId = None
        self.balance = 0
        self.accountHolderName = None
        self.pin = "qwertyuiop"
        
    def deposit(self,amount):
        self.balance+=amount
        self.saveToDatabase()
        print("Deposit Successful")


    def saveToDatabase(self):
        accountDetails = {
            "accountId": self.accountId,
            "balance": self.balance,
            "accountHolderName": self.accountHolderName,
            "pin": self.pin
        }
        tinyDBObject = TinyDB('db-account.json')
        q=Query()
        tinyDBObject.update(accountDetails,q.accountId==self.accountId)
        
        



    def withdraw(self,amount):
        
        if(amount<=self.balance):
            self.balance-=amount
            self.saveToDatabase()
            print("Withdrawl Successful")
        else:
            print("Not enough balance")

        
    def showBalance(self):
        print("Your Account balance is:")
        print(self.balance)

    def fileNewAccount(self):
        searchResult = self.searchAccountId(self.accountId)
        print("searchResult", searchResult)

        if len(searchResult) == 0:
            accountDetails = {
                "accountId": self.accountId,
                "balance": self.balance,
                "accountHolderName": self.accountHolderName,
                "pin": self.pin
            }
            tinyDBObject = TinyDB('db-account.json')
            tinyDBObject.insert(accountDetails)
            print("Account Created", self.accountId)
    
        else:
            print("Account Found => balance", self.accountHolderName)
            accountData = searchResult[0]

            # Ideally we would thorw an error but for sake 
            # of simplicity we move one with correct data
            self.accountId = accountData["accountId"]
            self.balance = accountData["balance"]
            self.accountHolderName = accountData["accountHolderName"]
            self.pin = accountData["pin"]
        
        print("Registration process complete.")

    def searchAccountId(self, accountId):
        tinyDBObject = TinyDB('db-account.json')

        q = Query()
        result = tinyDBObject.search(q.accountId == accountId)
        return result

