
# ATM Interface
The code is used to perform various transactions on an ATM once a user is verifed based on the ATM card number and a pin.


## How to Use
* Run the initialize.py to create some sample users in the database with various attributes. Pin is not initialized yet and will be set by the user upon first entry.
* Run atm.py
* Enter a card number. If it is present in database, proceed to enter the pin. If not, error message is displayed.
* If we enter card number for the first time, the code asks to set up a pin.
* Once the pin is set, it is no longer required to set it again on further entries.
* Now perform the desired transaction.

## Package Dependencies
* tinydb
* getpass
* os
* time
## Attributes in database
**Account:**
* Account Id
* Balance
* Account Holder Name

**Card:**
* Pin
* Card Number
* Bank Name
* CVV
* Expiry date 

**User:**
* Name
* Date of Birth
* Mobile Number
* User Id

## File Description
**user.py:**

* searchUser(): returns the details of the user whose user Id it receives.
* fileNewUser(): Adds the details of the user to the database using searchUser()
* searchCardNumber(): Returns details of the user who has entered his card.
* getAccountId(): Returns account Id of the user who uses his card.

**card.py:**

* searchCardNumber(): returns the details of the card whose card number it receives.
* fileNewCard(): Adds the details of the card to the database using searchCardNumber() of the **card** class
* searchCardNumber(): Returns details of the card inserted.
* savePinToDatabase(): Updates pin to database after it is set by the user on first entry.
* setNewPin(): Setes a new pin on first entry and saves it to database using savePinToDatabase()
* authenticateCardPin(): Authenticates a user based on his card number and pin. It also sets a pin if user enters for the first time.

**account.py:**
* saveToDatabase(): updates the changes in account balance upon deposit or withdrawl.
* deposit(): Updates the deposited amount in the database using saveToDatabase()
* withdraw(): Updates the withdrawn amount in the database using saveToDatabase()
* showBalance(): Displays the user's current account balance.
* searchAccountId(): Returns details of the account whose Id it receives.
* fileNewAccount(): Adds the details pf the account to the database using searchAccountId()

**initialize.py:**

* Sets up few accounts, cards and the respective users to test the program.
* These details are updated to the database using fileNewAccount(), fileNewCard(), fileNewUser()

**atm.py:**

* **To run the program after initializing, execute atm.py**
* performAccountInteractions(): Allows user to perform various transactions based on their choice.
* authorization(): Authenticates the user and allows the user to perform transactions using performAccountInteractions()
* printAtmMenu(): Simply prints the menu each time a user is Authenticated.







## Key Features
* The project uses tinydb to store details of users, card and account.
* To ensure that the pin is not visible while typing, getpass module is used.
* The code is basically a 24 x 7 ATM.
* After each transaction, user is asked to press 'c' in order to clear the details of his transaction so that they are not visible to the next user.
* If user enters a wrong pin three times in a row, authentication fails. 
* 2 seconds after the screen is cleared, a "Thank You" message is displayed and the next user is welcomed. This is achieved by the time module.
* The code in all files is perfectly clean as linting is done by flake8.
* requirements.txt is contains versions of packages used throughout the code.

