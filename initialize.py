#Creates 4 users and stores them to the database
from account import Account
from card import Card
from user import User
acc = Account()

# Set New Values
acc.accountId  = "acc1"
acc.balance = 1000
acc.accountHolderName = "Ram"

# Request New Registration
acc.fileNewAccount()


acc2 = Account()

acc2.accountId  = "acc2"
acc2.balance = 1000
acc2.accountHolderName = "Shyam"

# Request New Registration
acc2.fileNewAccount()


acc3 = Account()

acc3.accountId  = "acc3"
acc3.balance = 10000
acc3.accountHolderName = "Shyambabu"

# Request New Registration
acc3.fileNewAccount()



acc4 = Account()

acc4.accountId  = "acc4"
acc4.balance = 100000
acc4.accountHolderName = "Shyamsingh"

# Request New Registration
acc4.fileNewAccount()
#Creaating objects of card class


c1=Card()
c1.pin=None
c1.cardNumber=12345
c1.bankName='BITS bank'
c1.cvv=789
c1.expiryDate='11/23'
c1.fileNewCard()



c2=Card()
c2.pin=None
c2.cardNumber=43272
c2.bankName='BITS bank'
c2.cvv=578
c2.expiryDate='12/23'
c2.fileNewCard()



c3=Card()
c3.pin=None
c3.cardNumber=56835
c3.bankName='BITS bank'
c3.cvv=849
c3.expiryDate='02/24'
c3.fileNewCard()



c4=Card()
c4.pin=None
c4.cardNumber=56349
c4.bankName='BITS bank'
c4.cvv=598
c4.expiryDate='04/24'
c4.fileNewCard()




c5=Card()
c5.pin=None
c5.cardNumber=45359
c5.bankName='BITS bank'
c5.cvv=759
c5.expiryDate='07/24'
c5.fileNewCard()

#Creating objects of user class
'''
self.name=None
        self.dateOfBirth=None
        self.mobileNumber=None
        self.account=None
        self.card=None
        self.userId=None


'''
u1=User()
u1.account=acc
u1.card=c1
u1.name='Ram'
u1.dateOfBirth='12/12/1996'
u1.userId='21435'
u1.mobileNumber='6798567576'
u1.fileNewUser()


