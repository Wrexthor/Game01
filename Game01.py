from random import randint

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
        self.level = 1
        self.captured = False

    def add_traits(self, trait):
        self.traits.append(trait)

    def add_followers(self, follower, fame):
        self.followers.append(follower)
        self.fame + fame

    def add_item(self, item):
        self.inventory.append(item)

    def defend(self, dmg, count):
        # function for being attacked
        if self.check_follower():
            # there are followers, so run follower function
            if not self.damage_follower(dmg, count):
                return False
            else:
                return  True
        else:
            # no followers, run self function
            if not self.damage_self(dmg, count):
                return False
            else:
                return True

    def check_follower(self):
        # check if player has followers
        if self.followers > 0:
            return True
        else:
            return False

    def damage_follower(self, dmg, count):
        # get random follower from list
        random = randint(0, self.followers.__len__())

        # check if damage exceeds followers hp
        if dmg > self.followers[random].hp:
            self.remove_hp(random)
            # get more followers and damage them as well
        else:
            # damage only follower already collected
            self.followers[random].hp - dmg
            print (self.followers[random] + ' lost' + dmg + ' hp')

        # check if overwhelmed
        if self.check_overwhelmed(count):
            # overwhelmed is true, return false
            return False
        else:
            # overwhelmed is not true, return true
            return True

    def remove_hp(self, random):
            # follower is dead, remove it
            self.followers[random].remove()
            print(self.followers[random] + ' has died')

    def damage_self(self):
        result = False
        # get random
        random = randint(0, 10)
        # if random below 3, player is captured
        if random < 3:
            self.captured = True
            result = True
        # if random below 6 and above 3, player is injured
        if random > 3 & random < 6:
            self.traits
            result = True
        else:
            result = False
        return result


    def check_overwhelmed(self, count):
        # check if player has followers
        if self.check_follower():
            # checks if count of enemies is overwhelming the count of players army
            if self.followers.__len__() * 1.5 < count:
                # overwhelmed is false
                return True
            else:
                # overwhelmed is true
                return False
        else:
            # if more than 5 enemies and player solo
            if count > 7:
                # defeated
                return True
            else:
                # ok
                return  False



# dict of items
# need to define values of each item
# items = {'item1': [0, 0, 0]}

# dict of traits
# need to define values of each trait
traits = {'trait1': [0, 0, 0]}

# dict of npc's
# need to define values of each npc
# these can be used to create objects from class NPC at encounter time
# npcs = {'npc1': [0, 0, 0]}

# npc base class
# hit points variable (int)
# damage variable (int)
# name variable (string)
# amount variable (int)


class Npc:
    def __init__(self, name, description, fame_value, count):
        self.name = name
        self.description = description
        # amount of npc's
        self.count = count
        # base fame value for npc
        self.fame_value = fame_value
        # amount of fame value added, dependant on count
        self.fame_total = self.fame_value * self.count
        # hit points
        self.hp = 10


class Fighter(Npc):
    def __init__(self):
        self.fame_added = 5
        # damage done
        self.dmg = 10
        # morale, if 0 escapes
        self.morale = 10


class Merchant(Npc):
    def __init__(self):
        self.gold_added = 10


class Slave(Npc):
    def __init__(self):
        self.fear = 10


class Soldier(Fighter):
    def __init__(self, count):
        super().__init__(name='Soldier',
                         description='A trained soldier',
                         fame_value=3,
                         fear=20,
                         count=count)


class Gladiator(Fighter, Slave):
    def __init__(self, count):
        super().__init__(name='Gladiator',
                         description='A slave that fights until death, oftentimes for the entertainment of its master',
                         fame_value=4,
                         hp=10,
                         dmg=2,
                         morale=100,
                         fear=10,
                         count=count)


class Pleasure(Slave):
    def __init__(self, count):
        super().__init__(name='Pleasure Slave',
                         description='A slave whos existance is solely to give pleasure to others',
                         fame_value=3,
                         fear=20,
                         count=count)


# npc sub classes
# types available, slave, merchant, fighter, cheiftan

# menu class
# takes choice of player

# event class
# based on input parameters (like fame, dread etc)
# outputs events

p = Player()
slave = Pleasure(5)
p.name = input('What is your characters name?')
#
# Commands = {
#   'quit': Player.quit,
#   'help': Player.help,
#   'status': Player.status,
#   'rest': Player.rest,
#   'explore': Player.explore,
#   'flee': Player.flee,
#   'attack': Player.attack,
#   }
print('Type help for list of actions')

# game loop
while (True):
    print('inside the loop')
    print(p.name, p.fame, p.dread)