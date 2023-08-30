class Bank:
    def __init__(self, name: str, balance: float):
        self.name = name
        self.balance = balance
    
    def __repr__(self):
        print('{name}: {balance}'.format(name = self.name, balance = self.balance))
    
    def transfer(self, recipient, amount):
        if amount >= self.balance:
            self.balance -= amount
            recipient.balance += amount
            print('Transfer successfull!')
        else:
            print('Your balance does not cover that transfer!')

#Create an empty Database    
database = {}

#Initialise Database
print('Create the database.......')
while name := input('Enter your name or exit with pressing <return>: \n'):
    amount = float(input('Enter your current balance: \n'))
    database[name] = Bank(name, amount)

# Access Database
print('Now accessing the database.......')
while name := input('Enter a name or <return> to end: '):
    if (account := database.get(name)):
        action = input('What would you like to do? display, deposit or withdraw? ')
        if action in ('display', 'Display'):
            print(account)