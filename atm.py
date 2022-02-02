from account import Account

class Atm:

    
        
    def driver(self):
        flag=0
        while(flag==0):
            #id number verification
            acountInUse = None
            while True:
                accountTemp = Account()
                inputAccountNumber=input("enter account id")
                

                searchResult = accountTemp.searchAccountId(inputAccountNumber)

                if len(searchResult):
                    print(searchResult)
                    

                    pin=input("enter account pin")
                    
                    if pin == searchResult[0]['pin']:
                        acountInUse = accountTemp
                    else:
                        print("Bad Pin")
                        continue

                else:
                    print("Not Found")
                    continue
#press 2 to get account balance
#press 4 to exit transactions(remove card). Atm ni band krdena!Iss file se ho jayega.

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
                accountTemp = Account()
                inputAccountNumber=input("enter account id")
                

                searchResult = accountTemp.searchAccountId(inputAccountNumber)

                if len(searchResult):
                    print(searchResult)
                    

                    
                    count=0
                    while(count<3):
                        pin=input("enter account pin")
                        if pin == searchResult[0]['pin']:
                            print("Authenticated")
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
        
    def printAtmMenu():
        #Print Menu



atm = Atm()
atm.authorization()
#figure out requirements.txt and add it to your repo
#commit all files except .json to github
