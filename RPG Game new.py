# Importing needed libraries:
import random

# Create the player class
class player:
    # initialize a player class with a given name and auto-associated values
    def __init__(self, name: str, type: type):
        self.name = name
        self.level = 1
        self.health = self.level * 5
        self.max_health = self.level * 5
        self.is_knocked_out = False
        self.is_active = False
        self.type = type
        self.potions = {'health potion': 3}

    # Return the status and level of a player
    def __repr__(self):
        return ('{name} is a level {level} {type}.'.format(name = self.name, level = self.level, type = self.type))

# Original Attack Method:
    def attack(self, name):
        # Get the target from the given name of the enemy
        if players.get(name) != None:
            print('You shouldnt attack your mates! \n')
            return
        if enemies.get(name) == None:
            print('That enemy does not exist! \n')
            return
        target = players.get(name)
        if self.is_knocked_out == True:
            print('You are knocked out and cant attack! \n')
            return
        if self.type == 'Paladin':
            self.attack_bonus = 0
        elif self.type == 'Knight':
            self.attack_bonus = 2
        elif self.type == 'Mage':
            self.attack_bonus = 5
        attack_dice = random.randint(0, 20)
        attack_dice_bonus = attack_dice + self.attack_bonus
        print('The dices rolled a ' + str(attack_dice) + ' for attack !')
        print('Adding your bonus, you got a '+ str(attack_dice_bonus) + ' for attack!')
        if attack_dice_bonus <= 5:
            damage_dealt = 0
        elif attack_dice_bonus <= 15:
            damage_dealt = 3
        else:
            damage_dealt = 5
        target.lose_health(damage_dealt - target.defend())
    
    def defend(self):
        if self.is_knocked_out == True:
            print('You are knocked out and cant defend yourself! \n')
            return
        if self.type == 'Paladin':
            self.defence_bonus = 3
        elif self.type == 'Knight':
            self.defence_bonus = 2
        elif self.type == 'Mage':
            self.defence_bonus = 0
        defence_dice = random.randint(0, 20)
        defence_dice_bonus = defence_dice + self.defence_bonus
        print('The dices rolled a ' + str(defence_dice) + ' for defence!')
        print('Adding your bonus, you got a '+ str(defence_dice_bonus) + ' for defence!')
        if defence_dice_bonus <= 5:
            return 0
        elif defence_dice_bonus <= 15:
            return 1
        else:
            return 2
        
    def knock_out(self):
        self.is_knocked_out = True
        if self.health != 0:
            self.health = 0
        print('{name} has been knocked out and needs to be revived!'.format(name = self.name))
    
    def revive(self, name):
        if players.get(name) == None:
            print('That player does not exist. \n')
            return
        if enemies.get(name) != None:
            print('That enemy does not exist! \n')
            return
        target = players.get(name)
        if target.is_knocked_out == True:
            target.is_knocked_out = False
        if target.health != 1:
            target.health = 1
        print('{name} has been revived!'.format(name = self.name))

    def lose_health(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.health = 0
            self.knock_out()
        else:
            print('{name} has lost {amount} health and has now {health} health.'.format(name = self.name, amount = amount, health = self.health))
    
    def use_potion(self):
        print('Available potions: ' + str(self.potions.keys()))
        potion = input('Which potion do you want to use? \n')
        while potion not in self.potions.keys():
            potion = input('Sorry, that potion is not available. \n')
        name = input('Who do you want to use that potion on? \n')
        if players.get(name) == None:
            print('That player does not exist. \n')
            return
        if enemies.get(name) != None:
            print('That enemy does not exist! \n')
            return
        target = players.get(name)

# Databases:
players = {}
enemies = {}

# Ask player one for their name:
player_one_name = input('What is the name of the first player? \n')
# Let player one choose their type:
player_one_type = input(str(player_one_name) + ' has to choose their class out of those three: \nKnight, Paladin or Mage \n')
while player_one_type != 'Knight' and player_one_type != 'Paladin' and player_one_type != 'Mage':
    player_one_type = input('That class is not an option. Did you make a typo? \n')
# Creating the object of player one
players[player_one_name] = player(player_one_name, player_one_type)
print(players[player_one_name])
print('...')

# Ask player two for their name:
player_two_name = input('What is the name of the second player?\n')
# Let player one choose their type:
player_two_type = input(str(player_two_name) + ' has to choose their class out of those three: \nKnight, Paladin or Mage \n')
while player_two_type != 'Knight' and player_two_type != 'Paladin' and player_two_type != 'Mage':
    player_two_type = input('That class is not an option. Did you make a typo? \n')
# Creating the object of player two
players[player_two_name] = player(player_two_name, player_two_type)
print(players[player_two_name])
print('...')

players[player_one_name].attack(player_two_name)
