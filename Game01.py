from random import randint


class Game:
    def __init__(self):
        self.onward = False
        self.march = False
        self.camp = False

    def cmd_help(self):
        print('Commands available:'
              'help - lists all commands'
              'stats - shows player stats'
              'camp - make camp, unlocks further commands marked with *'
              'onward - moves player once, then makes camp'
              'march - automatically moves onward until supplies run out or player makes camp'
              '*forage - gathers supplies'
              '*motivate - increase troop motivation'
              '*whip - increase fear of slaves'
              'quit - exits game')


    def cmd_stats(self, player):
        # add more defintions
        print(player.fame,
              player.dread,
              player.supplies,
              player.followers.__len__(),
              player.followers,
              player.traits,
              player.captured)

    def cmd_camp(self):
        print('Player makes camp for the night..')
        self.camp = True

    def cmd_onward(self):
        print('Time to move forward')
        self.onward = True

    def cmd_march(self):
        print('Marching forward, stopping for no man!')
        self.march = True

    def cmd_forage(self, player):
        if self.camp:
            print('Lets get some supplies!')
            random = randint(1, 10)
            player.supplies + random
            print('Found ' + random + ' supplies')
        else:
            print('You need to make camp before attempting to forage.')

    def cmd_motivate(self, player):
        # check if camped and if followers present
        if self.camp & player.followers.__len__ > 0:
            print('I have a dream...')
            # add value between 1 and 3 to each follower
            for val in player.followers:
                if val.motivation == True:
                    random = randint(1, 3)
                    val.motivation + random
        else:
            print('You need to make camp and have some followers before attempting to motivate.')

    def cmd_whip(self, player):
        # check if camped and if followers present
        if self.camp & player.followers.__len__ > 0:
            print('Bow before me puny slaves!')
            # add value between 1 and 3 to each follower
            for val in player.followers:
                if val.fear == True:
                    random = randint(1, 3)
                    val.fear + random
        else:
            print('You need to make camp and have some slaves before attempting to whip them.')

    def cmd_quit(self):
        print('Please come again!')
        exit()


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

    def encounter_type(self):
        # determine type of encounter
        random = randint(1, 9)
        # type 1 fighting
        # type 2 merchant
        # type 3 distress
        type = 0
        # fighting encounter
        if random > 6:
            type = 1
        # merchant encounter
        if random <= 3:
            type = 2
        # distress encounter
        if random > 3 & random <= 6:
            type = 3
        return type

    def encounter_action(self, type):
        # depending on type, define encounter event
        if type == 1:
            print('And there was a firefight!')

        if type == 2:
            print('Do come back.')

        if type == 3:
            print('That princess sure could use some help..')

        def encounter_start():
            # run encounter
            self.encounter_action(self.encounter_type())


# event class
# based on input parameters (like fame, dread etc)
# outputs events

p = Player()
slave = Pleasure(5)
gladiator = Gladiator(100)
p.name = input('What is your characters name?')

print('Type help for list of actions')

# game loop
while (True):
    print('inside the loop')
    print(p.name, p.fame, p.dread)
    break