# player class
# fame variable (int)
# dread variable (int)
# supplies variable (int)
# inventory array (obj)
# traits variable (int)
# followers variable (int)
# name varaible (string)

class Player:
    def __init__(self):
        self.name = 'noName'
        self.dread = 0
        self.fame = 0
        self.supplies = 0
        self.inventory = []
        self.traits = []
        self.followers = []

    def addFame(self):
        self.fame + 1

    def addSupplies(self):
        self.supplies + 1

    def addDread(self):
        self.dread + 1

    def addTraits(self, trait):
        self.traits.append(trait)

    def addFollowers(self, follower):
        self.followers.append(follower)

    def addItem(self, item):
        self.inventory.append(item)

# dict of items
# need to define values of each item
items = {'item1': [0, 0, 0]}

# dict of traits
# need to define values of each trait
traits = {'trait1': [0, 0, 0]}

# dict of npc's
# need to define values of each npc
# these can be used to create objects from class NPC at encounter time
npcs = {'npc1': [0, 0, 0]}

# npc base class
# hit points variable (int)
# damage variable (int)
# name variable (string)
# amount variable (int)

# npc base class
class Npc:
    def __init__(self, name, hp, dmg, count):
        # name of npc
        self.name = name
        # description of npc
        self.description
        # hitpoints
        self.hp = hp
        # damage done
        self.dmg = dmg
        # amount of npc's
        self.count = count
        self.fame_added

class Merchant(Npc):
    def __init__(self):
        self.fame_added = 5
        self.gold_added = 10

# npc sub classes
# types available, slave, merchant, fighter, cheiftan

# menu class
# takes choice of player

# event class
# based on input parameters (like fame, dread etc)
# outputs events

p = Player()
p.name = input('What is your characters name?')

Commands = {
  'quit': Player.quit,
  'help': Player.help,
  'status': Player.status,
  'rest': Player.rest,
  'explore': Player.explore,
  'flee': Player.flee,
  'attack': Player.attack,
  }
print('Type help for list of actions')

# game loop
while (True):
    print('inside the loop')
    print(p.name, p.fame, p.dread)