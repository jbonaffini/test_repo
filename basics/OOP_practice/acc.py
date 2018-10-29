class Account:

    def __init__(self,filepath):
        self.filepath = filepath
        with open(self.filepath,'r') as file:
            self.balance=int(file.read())

    def withdraw(self, amount):
        self.balance= self.balance-amount

    def deposit(self, amount):
        self.balance= self.balance+amount

    def commit(self) :
        with open(self.filepath, 'w') as file :
            file.write(str(self.balance))

class Checking(Account):
    """This class generates checking account objects"""
    type="Checking"

    def __init__(self, filepath, fee):
        Account.__init__(self,filepath)
        self.fee=fee

    def transfer(self, amount) :
        self.balance=self.balance-amount-self.fee






filepath=r'D:\dev\practice_workspace\basics\OOP_practice\balance.txt'
# account= Account(filepath)
# print(account)
# print(account.balance)
# account.withdraw(100)
# print(account.balance)
# account.commit()
checking1= Checking(filepath,10)
# print(checking.balance)
# checking.deposit(100)
# print(checking.balance)
# checking.transfer(100)
# print(checking.balance)
print(checking1.type)

checking2= Checking(filepath,10)
print(checking2.type)
