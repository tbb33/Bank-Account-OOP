class Account:

    def __init__(self, filepath):
        with open(filepath, 'r') as file:
            self.balance=int(file.read()) #saves value of txt file inside instance var

account = Account("balance.txt") #may need to pass directory here for txt file
print(account) #output main - occur when execute script (differs when import)
print(account.balance) #can access attributes of obj instance using dot notation
