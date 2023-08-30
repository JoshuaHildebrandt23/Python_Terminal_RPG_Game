# #Importing needed libraries:
# import random

# #Create the player class
# class player:
#   #initialize a player class with a given name and auto-associated values
#   def __init__(self, name: str, type: type):
#     self.name = name
#     self.level = 1
#     self.health = self.level * 5
#     self.max_health = self.level * 5
#     self.is_knocked_out = False
#     self.is_active = False
#     self.type = type
#     self.potions = {'health potion': 3}

#   def __repr__(self):
#     print('{name} is a level {level} {type}.'.format(name = self.name, level = self.level, type = self.type))

  def attack(self, name):
    # Get the target from the given name of the enemy
    if enemies.get(name) == None:
      print('That enemy does not exist! \n')
      return
    target = enemies.get(name)
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

  def defend(self):
    if self.is_knocked_out == True:
      print('You are knocked out and cant defend yourself!')
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
  
  def revive(self, target):
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
    target = input('Who do you want to use that potion on? \n')
    while target != players[name].name and target != enemy_two.name and target != player_one.name and target != player_two.name:
      target = input('This person does not exist. Please choose another one. \n')
          
# Create class for enemies:
class enemy:
  def __init__(self, name: str,level: int, type: type):
    self.name = name
    self.level = 1
    self.health = self.level * 5
    self.max_health = self.level * 5
    self.is_knocked_out = False
    self.is_active = False
    self.type = type
# Class tells their name, level and type
  def __repr__(self):
    print('{name} is a level {level} {type}.'.format(name = self.name, level = self.level, type = self.type))
# Create attack move
  def attack(self):
    #Choose the player that the enemy will attack
    if player_one.type == 'Paladin':
      target = player_one
    elif player_two == 'Paladin':
      target = player_two
    else:
      random_target_num = random.randint(1, 2)
      if random_target_num == 1:
        target = player_one
      else:
        target = player_two

    if self.is_knocked_out == True:
      print('You are knocked out and cant attack!')
      return
    if self.type == 'Paladin':
      self.attack_bonus = 0
    elif self.type == 'Knight':
      self.attack_bonus = 1
    elif self.type == 'Mage':
      self.attack_bonus = 2
    attack_dice = random.randint(0, 18)
    attack_dice_bonus = attack_dice + self.attack_bonus
    print('The dices rolled a ' + str(attack_dice) + ' for attack !')
    print('Adding their bonus, they got a '+ str(attack_dice_bonus) + ' for attack!')
    if attack_dice_bonus <= 5:
      damage_dealt = 0
    elif attack_dice_bonus <= 15:
      damage_dealt = 3
    else:
      damage_dealt = 5
    target.lose_health(damage_dealt - target.defend())

# Create defence stats
  def defend(self):
    if self.is_knocked_out == True:
      print('You are knocked out and cant defend yourself!')
      return
    if self.type == 'Paladin':
      self.defence_bonus = 2
    elif self.type == 'Knight':
      self.defence_bonus = 1
    elif self.type == 'Mage':
      self.defence_bonus = 0
    defence_dice = random.randint(0, 20)
    defence_dice_bonus = defence_dice + self.defence_bonus
    print('The dices rolled a ' + str(defence_dice) + ' for defence!')
    print('Adding their bonus, they got a '+ str(defence_dice_bonus) + ' for defence!')
    if defence_dice_bonus <= 5:
      return 0
    elif defence_dice_bonus <= 15:
      return 1
    else:
      return 2

# Function to knock out when health is 0 or below
  def knock_out(self):
    self.is_knocked_out = True
    if self.health != 0:
      self.health = 0
    print('{name} has been knocked out and can not fight anymore!'.format(name = self.name))

# Function to lose health
  def lose_health(self, amount):
    self.health -= amount
    if self.health <= 0:
      self.health = 0
      self.knock_out()
    else:
      print('{name} has lost {amount} health and has now {health} health.'.format(name = self.name, amount = amount, health = self.health))

# #Databases:
# players = {}
# enemies = {}
# 
# #Ask player one for their name:
# player_one_name = input('What is the name of the first player? \n')
# #Let player one choose their type:
# player_one_type = input('Narrator: ' + str(player_one_name) + ' has to choose their class out of those three: \nKnight, Paladin or Mage \n')
# while player_one_type != 'Knight' and player_one_type != 'Paladin' and player_one_type != 'Mage':
#   player_one_type = input('That class is not an option. Did you make a typo? \n')
# #Creating the object of player one
# players[player_one_name] = player(player_one_name, player_one_type)
# print('Player One is named {name} and is playing as {type}.'.format(name = players[name].name, type = players[name].type))
# print('...')
# #Ask player two for their name:
# player_two_name = input('What is the name of the second player? \n')
# #Let player two choose their type:
# player_two_type = input('Narrator: ' + str(player_two_name) + ' has to choose their class out of those three: \nKnight, Paladin or Mage \n')
# while player_two_type != 'Knight' and player_two_type != 'Paladin' and player_two_type != 'Mage':
#   player_two_type = input('That class is not an option. Did you make a typo? \n')
# #Create the object of player two
# players[player_two_name] = player(player_two_name, player_two_type)
# print('Player Two is named {name} and is playing as {type}.'.format(name = player_two.name, type = player_two.type))
# print('...')


#Create 2 Enemies:
enemies['Viktor'] = enemy('Viktor', 1, 'Paladin')
enemies['Hector'] = enemy('Hector', 1, 'Knight')

print('You spot 2 enemies! Due to your enourmous skill-level, you can detect their info! ')
print('The first enemy is {name}, a level {level} {type} !'.format(name = enemy_one.name, level = enemy_one.level, type = enemy_one.type))
print('The second enemy is {name}, a level {level} {type} !'.format(name = enemy_two.name, level = enemy_two.level, type = enemy_two.type))
while not (player_one.is_knocked_out == True and player_two.is_knocked_out == True):
  player_one_action_choice = input('What do you want to do first? \nYou can use one of your potions with "use_potion" \nYou can attack with "attack \n"')
  while player_one_action_choice != 'use_potion' and player_one_action_choice != 'attack':
    player_one_action_choice = input('Sorry, you cant do that.')
  if player_one_action_choice == 'use_potion':
    player_one.use_potion()
  elif player_one_action_choice == 'attack':
    target = input('Who do you want to attack?: \n')

