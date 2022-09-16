class BankAccount(object):
    def __init__(self, owner, account_number, account_type, balance):
        self.owner = str(owner)
        self.account_number = str(account_number)
        self.account_type = str(account_type)
        self.balance = float(balance)
        

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def __repr__(self):
        return f"owner: {self.owner} \n Acc No: {self.account_number} \n Balance: {self.balance}"
          
class Bank(object):
       def __init__(self, name, accounts):
        self.name = str(name)
        self.accounts = dict(accounts)


class Customer(object):
       def __init__(self, name, accounts):
        self.name = str(name)
        self.accounts = dict(accounts)

class Transactions():
     def __init__(self, account, amount, type):
        self.account = str(account)
        self.amount = float(amount)
    

# new objects
MohamedAccount = BankAccount("Mohamed", "Mo20222050", "Current", 100000)

absaBank = Bank()

Mohamed = Customer()


Cheque = Transactions()


print(MohamedAccount.owner)
   