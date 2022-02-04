# Creates 4 accounts, users and cards and stores them to the database
from account import Account
from card import Card
from user import User
# Creating objects of Account class and initializing their attributes
acc = Account()


acc.accountId = "acc1"
acc.balance = 1000
acc.accountHolderName = "Ram"

# Request New Registration
acc.fileNewAccount()


acc2 = Account()

acc2.accountId = "acc2"
acc2.balance = 1000
acc2.accountHolderName = "Shyam"

# Request New Registration
acc2.fileNewAccount()


acc3 = Account()

acc3.accountId = "acc3"
acc3.balance = 10000
acc3.accountHolderName = "Shyambabu"

# Request New Registration
acc3.fileNewAccount()

# Creating account 4
acc4 = Account()
acc4.accountId = "acc4"
acc4.balance = 100000
acc4.accountHolderName = "Shyamsingh"

# Request New Registration
acc4.fileNewAccount()
# Creaating objects of Card class and initializing their attributes

# Creating card 1
c1 = Card()
c1.pin = None
c1.cardNumber = 12345
c1.bankName = 'BITS bank'
c1.cvv = 789
c1.expiryDate = '11/23'
c1.fileNewCard()

# Creating card 2
c2 = Card()
c2.pin = None
c2.cardNumber = 43272
c2.bankName = 'BITS bank'
c2.cvv = 578
c2.expiryDate = '12/23'
c2.fileNewCard()


# Creating card 3
c3 = Card()
c3.pin = None
c3.cardNumber = 56835
c3.bankName = 'BITS bank'
c3.cvv = 849
c3.expiryDate = '02/24'
c3.fileNewCard()


# Creating card 4
c4 = Card()
c4.pin = None
c4.cardNumber = 56349
c4.bankName = 'BITS bank'
c4.cvv = 598
c4.expiryDate = '04/24'
c4.fileNewCard()


# Creating objects of User class and initializing their attributes


u1 = User()
u1.account = acc
u1.card = c1
u1.name = 'Ram'
u1.dateOfBirth = '12/12/1996'
u1.userId = '21435'
u1.mobileNumber = '6798567576'
u1.fileNewUser()

u2 = User()
u2.account = acc2
u2.card = c2
u2.name = 'Shyam'
u2.dateOfBirth = '1/11/1994'
u2.userId = '34743'
u2.mobileNumber = '9846675454'
u2.fileNewUser()

u3 = User()
u3.account = acc3
u3.card = c3
u3.name = 'Raj'
u3.dateOfBirth = '23/07/2000'
u3.userId = '79858'
u3.mobileNumber = '7545867576'
u3.fileNewUser()

u4 = User()
u4.account = acc4
u4.card = c4
u4.name = 'Neha'
u4.dateOfBirth = '16/09/1998'
u4.userId = '57734'
u4.mobileNumber = '6980658794'
u4.fileNewUser()
