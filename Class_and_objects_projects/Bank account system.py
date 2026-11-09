
#------------------------------------------------------------------------------------------------------
#BANK ACCOUNT
class BankAccount:
    def __init__(self,account_number,owner_name,balance=0):
        self.account_number=account_number
        self.owner_name=owner_name
        #self._balance=balance # _balance is a "protected" attribute. Convention: don't access directly.
        self.balance=balance
        self.transaction_history=[]

    # -------------------------------
    # Getter for balance
    # -------------------------------
    # Using @property allows us to read the balance safely.
    # Instead of accessing _balance directly, we call account.balance
    # This is part of encapsulation: we hide the real data and provide controlled access.
   # @property
    '''def balance(self):
        return self._balance

    # -------------------------------
    # Setter for balance
    # -------------------------------
    # Using @balance.setter allows us to control changes to the balance.
    # Example: prevent negative balances.
    # Any change to balance must go through this setter, otherwise rules won't be enforced.
    # Note: In Python, this does not completely block direct access to _balance,
    # but it's a strong convention: other developers should NOT touch _balance directly.
    @balance.setter
    def balance(self, value):
        if value < 0:
            print(" the balance cannot be negative.!")
        else:
            self._balance = value'''

    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            self.transaction_history.append(amount)
            print(f'{amount} deposited.New balance {self.balance}')
        else:
            print("Deposited a negative amount.")

    def withdraw(self,amount):
        if amount>self.balance:
            print('Insufficient funds.')
        elif amount<=0:
            print("Transacted a negative amount.")
        else:
            self.balance-=amount
            self.transaction_history.append(f'Withdrew: {amount}')
            print(f'{amount} withdrawn.New balance {self.balance}')
    def transfer(self,amount,other_account):
        if amount>self.balance:
            print('Insufficient funds.')
        elif amount<=0:
            print("Transacted a negative amount.")
        else:
            self.balance-=amount
            other_account.balance+=amount
            self.transaction_history.append(f'Transferred {amount} to {other_account.owner_name}.')
            other_account.transaction_history.append(f'Received {amount} from {self.owner_name}.')
            print(f'{amount} transferred to {other_account.owner_name}.')
            print(f'Received {amount} from {self.owner_name}.')


    def show_balance(self):
        print(f'Balance for {self.owner_name}: {self.balance}')
    def show_transaction_history(self):
        print(f'Transaction history for {self.owner_name}:')
        for transaction in self.transaction_history:
            print('->',transaction)



class SavingsAccount(BankAccount):
    def __init__(self,account_number,owner_name,balance=0,interest_rate=0.07):
        super().__init__(account_number,owner_name,balance)
        self.interest_rate=interest_rate
    def add_interest(self):
        interest= int(self.interest_rate * self.balance)
        self.balance+=interest
        self.transaction_history.append(f'Interested in {self.owner_name}: {interest}')
        print(f'{interest} interested to {self.owner_name}.')
    def saving_deposit(self,amount):
        self.balance+=amount
        self.transaction_history.append(f"Savings deposited {amount}.")
        print(f'{amount} for savings deposited for {self.owner_name}: {self.balance}')





#testing the Bank account and saving account





# Create accounts
acc1 = BankAccount("1001", "John", 500)
acc2 = BankAccount("1002", "Mary", 300)

# Deposit and withdraw
acc1.deposit(200)
acc2.withdraw(50)

# Transfer
acc1.transfer(150, acc2)

# Show info
acc1.show_balance()

acc2.show_balance()

acc1.show_transaction_history()

acc2.show_transaction_history()

savings = SavingsAccount("1001", "ken", 2000)
savings.saving_deposit(200)
savings.add_interest()
savings.balance
savings.show_balance()
savings.show_transaction_history()
