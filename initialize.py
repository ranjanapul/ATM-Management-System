#Creates 4 users and stores them to the database
from account import Account
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