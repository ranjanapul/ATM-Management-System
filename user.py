from tinydb import TinyDB, Query


class User:
    def __init__(self):
        self.name = None
        self.dateOfBirth = None
        self.mobileNumber = None
        self.account = None
        self.card = None
        self.userId = None

    def fileNewUser(self):
        searchResult = self.searchUser(self.userId)
        print("searchResult", searchResult)

        if len(searchResult) == 0:
            userDetails = {
                'accountId': self.account.accountId,
                'cardNumber': self.card.cardNumber,
                'name': self.name,
                'dateOfBirth': self.dateOfBirth,
                'mobileNumber': self.mobileNumber,
                'userId': self.userId
            }
            tinyDBObject = TinyDB('db-user.json')
            tinyDBObject.insert(userDetails)
            print("User Created ", self.userId)

        else:
            print("User Found", self.account.accountId)
        print("Registration process complete.")

    def searchUser(self, userId):
        tinyDBObject = TinyDB('db-user.json')

        q = Query()
        result = tinyDBObject.search(q.userId == userId)
        return result

    def searchCardNumber(self, cardNumber):
        """[summary]

        Args:
            cardNumber ([type]): [description]

        Returns:
            [type]: [description]
        """
        tinyDBObject = TinyDB('db-user.json')
        q = Query()
        result = tinyDBObject.search(q.cardNumber == cardNumber)
        return result

    def getAccountId(self):
        cardNumber = self.card.cardNumber
        result = self.searchCardNumber(cardNumber)
        if(len(result) == 1):
            return result[0]['accountId']
        else:
            return False
