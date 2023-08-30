# StoreSimulator

class Store:
    def __init__(self, name: str, balance: float, inventory: dict):
        self.name = name
        self.balance = balance
        self.inventory = inventory

class Shopper:
    def __init__(self, name: str, balance: float):
        self.name = name
        self.balance = balance
        self.inventory = {}
    # def purchase(self, Store, items: str):
    #     self.items = items

#Assuming a store has an infinite amount of its products available
Store_1 = Store('Electronics', 2000, {'TV': 500, 'Smartphone': 400, 'Videogame': 60})
Store_2 = Store('Food', 2000, {'Apple': 2, 'Banana': 5, 'Milk': 4})

Store_db = [Store_1, Store_2]
Shopper_db = {}

print('Create new Shopper.....')
name = input('What is your name? \n')
amount = float(input('What is your current balance?: \n'))
Shopper_db[name] = Shopper(name, amount)

while True:
    Store = input('Where do you want to go shopping? \n')
    items = input('What item do you want to buy?')
    print(Shopper_db)
