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
    """This class generates checking account objects"""

    type="checking" #class var

    def __init__(self, filepath, fee):
        #call init from Account class -> creates min obj
        Account.__init__(self,filepath)
        self.fee=fee #creating instance var

    def transfer(self, amt):
        self.balance = self.balance - amt - self.fee

#first obj instance
jill_checking=Checking("jill.txt", 5) #instantiation class
jill_checking.deposit(10) #accessing method of base class
jill_checking.transfer(100)
print(jill_checking.balance) #instance var balance inherited from base class
jill_checking.commit()
print(jill_checking.type) #accessing attribute of obj

#second obj instance
jack_checking=Checking("jack.txt", 5)
jack_checking.deposit(10)
jack_checking.transfer(100)
print(jack_checking.balance)
jack_checking.commit()

#useful when import class from modules - provide info about class
print(jack_checking.__doc__)
