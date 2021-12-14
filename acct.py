class Account:

    def __init__(self, filepath):
        self.newfilepath=filepath #instance var to be use anywhere in script
        with open(filepath, 'r') as file:
            self.balance=int(file.read()) #saves value of txt file inside instance var

    def withdraw(self, amount):
        self.balance=self.balance-amount

    def deposit(self, amount):
        self.balance=self.balance+amount

    def commit(self):
        with open(self.newfilepath, 'w') as file:
            file.write(str(self.balance))

# account = Account("balance.txt") #may need to pass directory here for txt file
# print(account) #output main - occur when execute script (differs when import)
# print(account.balance) #can access attributes of obj instance using dot notation
# account.withdraw(100)
# print(account.balance)
# account.commit() #implicitely pass obj instance
# account.deposit(200)
# print(account.balance)
# account.commit()

#use inheritance to create subclass
class Checking(Account): #pass name of base class
    def __init__(self, filepath, fee):
        #call init from Account class -> creates min obj
        Account.__init__(self,filepath)
        self.fee=fee #creating instance var

    def transfer(self, amt):
        checking.balance = checking.balance - amt - self.fee


checking=Checking("balance.txt", 5) #passing 5 for fee value
checking.deposit(10) #accessing method of base class
print(checking.balance) #instance var balance inherited from base class
checking.commit()
checking.transfer(100)
print(checking.balance)
checking.commit()
