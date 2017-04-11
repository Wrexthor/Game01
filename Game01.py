from random import randint
import time, threading, os


'''
Program synopsis
Written by Jack Swedjemark

Text based RPG where action is automated and more ephasis is placed on
the story and events occuring.


Classes
Player - stores stats of player, list of npcs, items and traits
and calculates combat based on stats

NPC - stores npc stats

Items - stores item stats
 
Game - keeps track of user input, game state adn time simulations

Event - Calculates event types, actions and chances using NPC and player stats, 
calling player methods
'''

'''
def background(q):
    while True:
        stuff = input()
        print('Recieved ' + stuff)
        q.put(stuff)
'''



class Game:
    def __init__(self, player):
        self.onward = False
        # self.march = False
        self.camp = False
        self.input = 'empty'
        self.player = player

    def run(self):
        t1 = threading.Thread(target=self.listen)
        t1.start()

    def listen(self):
        while True:
            # get user input
            self.input = input()
            # debug
            print('Recived ' + self.input)
            self.check_listen()

    def check_listen(self):
        # check what input command is and executes if matching
        # any of the commands
        if self.input == 'help':
            self.cmd_help()
            self.input = 'empty'
        if self.input == 'stats':
            self.cmd_stats()
            self.input = 'empty'
        if self.input == 'camp':
            self.cmd_camp()
            self.input = 'empty'
        if self.input == 'onward':
            self.cmd_onward()
            self.input = 'empty'
        if self.input == 'march':
            self.cmd_march()
            self.input = 'empty'
        if self.input == 'forage':
            self.cmd_forage()
            self.input = 'empty'
        if self.input == 'motivate':
            self.cmd_motivate()
            self.input = 'empty'
        if self.input == 'whip':
            self.cmd_whip()
            self.input = 'empty'
        if self.input == 'quit':
            self.cmd_quit()
            self.input = 'empty'
        else:
            if not self.input == 'empty':
                print('Unknown command')

    def cmd_help(self):
        # print list of commands available to player
        print('Commands available:\n'
              'help - lists all commands\n'
              'stats - shows player stats\n'
              'camp - make camp, unlocks further commands marked with *\n'
              'onward - moves player once, then makes camp\n'
              'march - automatically moves onward until supplies run out or player makes camp\n'
              '*forage - gathers supplies\n'
              '*motivate - increase troop motivation\n'
              '*whip - increase fear of slaves\n'
              'quit - exits game\n')

    def cmd_stats(self):
        # add more defintions
        print(self.player.fame,
              self.player.dread,
              self.player.supplies,
              self.player.count,
              self.player.followers,
              self.player.traits,
              self.player.captured)

    def cmd_camp(self):
        print('Player makes camp for the night..')
        self.camp = True

    def cmd_onward(self):
        print('Player moves forward.')
        self.onward = True
        self.camp = False

    def cmd_march(self):
        print('Player breaks camp and begins marching.')
        # self.march = True
        self.camp = False

    def cmd_forage(self):
        if self.camp:
            print('Lets get some supplies!')
            random = randint(1, 10)
            self.player.supplies + random
            print('Found ' + random + ' supplies')
        else:
            print('You need to make camp before attempting to forage.')

    def cmd_motivate(self):
        # check if camped and if followers present
        if self.camp & self.player.followers.__len__ > 0:
            print('Player motivates his followers: I have a dream...')
            # add value between 1 and 3 to each follower
            for val in self.player.followers:
                if val.motivation == True:
                    random = randint(1, 3)
                    val.motivation + random
        else:
            print('You need to make camp and have some followers before attempting to motivate.')

    def cmd_whip(self):
        # check if camped and if followers present
        if self.camp & self.player.followers.__len__ > 0:
            print('Player takes out his whip: Kneel slaves!')
            # add value between 1 and 3 to each follower
            for val in self.player.followers:
                if val.fear == True:
                    random = randint(1, 3)
                    val.fear + random
        else:
            print('You need to make camp and have some slaves before attempting to whip them.')

    def cmd_quit(self):
        print('Please come again!')
        os._exit(1)


class Player:
    def __init__(self):
        self.name = 'noName'
        self.dread = 0
        self.fame = 0
        self.supplies = 0
        self.inventory = []
        self.traits = []
        self.followers = []
        self.count = self.followers.__len__()
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
        random = randint(0, self.count)

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

    def damage_self(self, traits):
        result = False
        # get random
        random = randint(0, 10)
        # if random below 3, player is captured
        if random < 3:
            self.captured = True
            result = True
        # if random below 6 and above 3, player is injured
        if random > 3 & random < 6:
            # need to llok up how to get random index of a dictionary with lists !!!!!!!!!!!
            #self.traits + traits[(randint(0,10))]
            #print('Player was injured, ' + traits[(randint(0, 10))] + ' was added')
            result = True
        else:
            result = False
        return result

    def calc_traits(self, trait):
        self.dread + trait[3]
        self.fame + trait[4]
        self.supplies + trait[5]

    def check_overwhelmed(self, count):
        # check if player has followers
        if self.check_follower():
            # checks if count of enemies is overwhelming the count of players army
            if self.count * 1.5 < count:
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

'''
dict of traits
value 0 in list is effect on health
value 1 is effect on damage
value 2 is effect on morale
value 3 is effect on dread
value 4 is effect on fame
value 5 is effect on supplies
'''

traits = {'Broken Leg': [-2, 0, 0, -5, 0, -1], 'Fever': [-2, -2, -4, 1, 0, 0]}


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


class Fighter(Npc):
    def __init__(self, name, description, fame_value, count, dmg, morale, hp):
        # damage done
        self.dmg = dmg
        # morale, if 0 escapes
        self.morale = morale
        # hit points
        self.hp = hp
        super().__init__(name, description, fame_value, count)


class Merchant(Npc):
    def __init__(self):
        self.gold_added = 10

        super().__init__(name='Merchant',
                         description='Providing anything you need, if the price is right..',
                         fame_value=3)


class Slave(Npc):
    def __init__(self, name, description, fame_value, count):
        self.fear = 10
        super().__init__(name, description, fame_value, count)


class Soldier(Fighter):
    def __init__(self, count):
        super().__init__(name='Soldier',
                         description='A trained soldier',
                         fame_value=3,
                         morale=20,
                         count=count)


class Gladiator(Fighter, Slave):
    def __init__(self, count):
        self.count = count
        super().__init__(name='Gladiator',
                         description='A slave that fights until death, oftentimes for the entertainment of its master',
                         fame_value=4*count,
                         count=count,
                         hp=10*count,
                         dmg=2*count,
                         morale=10)


class Pleasure(Slave):
    def __init__(self, count):
        super().__init__(name='Pleasure Slave',
                         description='A slave whos existance is solely to give pleasure to others',
                         fame_value=3,
                         count=count)

class Event:

    def __init__(self, player):
        self.player = player
        self.count = 0

    def encounter_type(self):
        # determine type of encounter
        random = randint(1, 9)
        # type 1 fighting
        # type 2 merchant
        # type 3 distress
        type = 0
        # fighting encounter
        if random > 5:
            type = 1
        # merchant encounter
        if random <= 2:
            type = 2
        # distress encounter
        if random > 2 and random <= 5:
            type = 3
        return type

    def encounter_action(self, type):
        # depending on type, define encounter event
        if type == 1:
            print('Player meets a gang of bandits, time to dull that blade of yours!')
            self.encounter_fight()

        if type == 2:
            print('Player meets a merchant, greed plain in his eyes.')

        if type == 3:
            print('Player sees a damsel conveniently in distress, time to comb those eyebrows!')

    def encounter_start(self):
        # calculate how many enemies
        self.calculate_count()
        type = self.encounter_type()
        # run encounter
        self.encounter_action(type)

    def calculate_count(self):
        # used to calculate how many enemies there are
        followers = self.player.count
        if followers > 0:
            # more than 1 follower, calculate count based of followers
            self.count = (followers * 100) / randint(70, 130)

        else:
            # no followers, chose random as count
            self.count = randint(1, 75)

    def encounter_fight(self):
        random = randint(1, 10)
        if random > 0 and random < 7:
            npc = Soldier(self.count)
            self.player.defend(npc.dmg, self.count)
        if random > 6 and random < 10:
            npc = Gladiator(self.count)
            self.player.defend(npc.dmg, self.count)

p = Player()
slave = Pleasure(5)
gladiator = Gladiator(100)
p.name = input('What is your characters name?')
g = Game(p)
e = Event(p)
g.run()

print('Type help for list of actions')

# game loop
while True:
    # check if onward, if it is, run encounter and make camp
    if g.onward:
        g.onward = False
        e.encounter_start()
        g.cmd_camp()
    # check if camped
    if not g.camp:
        # run an encounter
        e.encounter_start()
        time.sleep(5)
