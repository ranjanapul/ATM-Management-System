from tinydb import TinyDB, Query
from getpass import getpass


class Card:
    def __init__(self):
        # pin,card number,bank name,cvv,expiry date,
        self.pin = None
        self.cardNumber = None
        self.bankName = None
        self.cvv = None
        self.expiryDate = None

    def fileNewCard(self):
        searchResult = self.searchCardNumber(self.cardNumber)
        print("searchResult", searchResult)

        if len(searchResult) == 0:
            cardDetails = {
                'pin': self.pin,
                'cardNumber': self.cardNumber,
                'bankName': self.bankName,
                'cvv': self.cvv,
                'expiryDate': self.expiryDate
            }
            tinyDBObject = TinyDB('db-card.json')
            tinyDBObject.insert(cardDetails)
            print("Card Created ", self.cardNumber)
        else:
            print("Card Found")
        print("Registration process complete.")

    def searchCardNumber(self, cardNumber):
        tinyDBObject = TinyDB('db-card.json')

        q = Query()
        result = tinyDBObject.search(q.cardNumber == cardNumber)
        return result

    def setNewPin(self):
        newPin = int(input('Welcome, Set a pin '))
        self.pin = newPin
        self.savePinToDatabase()

    def savePinToDatabase(self):
        cardDetails = {
            'pin': self.pin,
            'cardNumber': self.cardNumber,
            'bankName': self.bankName,
            'cvv': self.cvv,
            'expiryDate': self.expiryDate
        }
        tinyDBObject = TinyDB('db-card.json')
        q = Query()
        tinyDBObject.update(cardDetails, q.cardNumber == self.cardNumber)

    def authenticateCardPin(self):
        inputCardNumber = int(input("enter card number "))
        result = self.searchCardNumber(inputCardNumber)
        if len(result) == 0:
            print('Wrong Card Number.Try again  ')
            return False
        else:
            self.pin = result[0]['pin']
            self.cardNumber = result[0]['cardNumber']
            self.bankName = result[0]['bankName']
            self.cvv = result[0]['cvv']
            self.expiryDate = result[0]['expiryDate']
        if self.pin is None:
            self.setNewPin()
        count = 0
        while(count < 3):
            print("Enter account pin ")
            pin = getpass()
            if str(pin) == str(self.pin):
                print("Authenticated")
                return True
            else:
                if(count != 2):
                    print("Bad Pin.Try again")
                count += 1
            if(count == 3):
                return False
