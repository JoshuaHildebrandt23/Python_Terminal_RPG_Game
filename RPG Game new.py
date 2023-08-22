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

## Original Attack Method:
    def attack(self, name):
        # Get the target from the given name of the enemy
        # if players.get(name) != None:
        #     print('You shouldnt attack your mates!')
        #     return
        # if enemies.get(name) == None:
        #     print('That enemy does not exist! \n')
        #     return
        target = players.get(name)
        if self.is_knocked_out == True:
            print('You are knocked out and cant attack!')
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
