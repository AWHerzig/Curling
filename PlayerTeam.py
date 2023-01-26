import names
import random
from Spot import pythag


class Player:  # Just as there are int objects and string objects, we make our own for Players
    def __init__(self, name):
        self.name = name  # Gets passed in at the instantiation of the player object
        self.xAcc = random.randrange(1, 11)  # Accuracy in the x direction (width), logarithmic growth in effect
        self.yAcc = random.randrange(1, 11)  # y (depth) accuracy, log
        self.sweep = random.randrange(1, 11)  # How much sweeping effects stone velocity, square root
        self.smart = random.randrange(1, 11)  # Ability to predict the natural stopping point of a stone in motion, log
        self.controlled = False  # Flag for User control, will be set to True

    def sweepDec(self, rock, sight, side):  # Decision-making on whether to sweep/not at any point. Called from Sheet(145)
        if sight:  # May or may not be able to see where the stone is going based on smart level
            spotFinal = rock.path()  # Depth and Width of where it will naturally end up if only affected by friction
            if self.controlled:  # Need User Decision
                try:
                    return int(input('Depth: '+str(round(spotFinal[0], 1))+', Width: '+str(round(spotFinal[1], 1))+'. 0 for nothing, 1 for '+side+' x, 2 for increase y, 3 for lil o both'))
                except ValueError:  # If they mess up the input (like just hitting enter), the whole code would break stopping all progress
                    return 0  # so just say don't sweep instead
            else:  # I try
                upSweep = rock.target[0] > spotFinal[0]
                if side == 'increase':
                    sideSweep = rock.target[1] > spotFinal[1]
                else:
                    sideSweep = rock.target[1] < spotFinal[1]
                if upSweep and sideSweep:
                    return 3  # Lil o both
                elif upSweep:
                    return 2  # Sweep ahead to speed up
                elif sideSweep:
                    return 1  # Sweep it to the side
                else:
                    return 0

        else:  # Blind
            if self.controlled:
                try:
                    return int(input('Depth: ___, Width: ___. 0 for nothing, 1 for '+side+' x, 2 for increase y, 3 for lil o both'))
                except ValueError:
                    return 0
            else:
                return 0


class Team:
    def __init__(self, name, ABR):
        self.name = name
        self.ABR = ABR
        self.roster = [Player(names.get_full_name()), Player(names.get_full_name()), Player(names.get_full_name()), Player(names.get_full_name())]
        self.Lead = None
        self.Second = None
        self.Third = None
        self.Skip = None
        self.picker()
        self.color = None  # Will be 'Blue' or 'Red' assigned at each game
        # Numbers stuffs
        self.wins = 0
        self.tWins = 0
        self.played = 0
        self.pD = 0
        self.tPD = 0
        self.teamX = 0
        self.teamY = 0
        self.teamSweep = 0
        self.teamSmart = 0
        for i in self.roster:
            self.teamX += i.xAcc
            self.teamY += i.yAcc
            self.teamSweep += i.sweep
            self.teamSmart += i.smart
        self.sStr = str(self.teamX)+' '+str(self.teamY)+' '+str(self.teamSweep)+' '+str(self.teamSmart)

    def __str__(self):
        return self.name

    def picker(self):
        maxSmort = 0
        indSmort = 0
        for i in range(4):
            if self.roster[i].smart > maxSmort:
                maxSmort = self.roster[i].smart
                indSmort = i
        self.Skip = self.roster[indSmort]
        maxSweep = 0
        indSweep = 0
        for i in range(4):
            if self.roster[i].smart > maxSweep and i != indSmort:
                maxSweep = self.roster[i].sweep
                indSweep = i
        self.Lead = self.roster[indSweep]
        maxAcc = 0
        indAcc = 0
        for i in range(4):
            if pythag(self.roster[i].xAcc, self.roster[i].yAcc) > maxAcc and i != indSmort and i != indSweep:
                maxAcc = pythag(self.roster[i].xAcc, self.roster[i].yAcc)
                indAcc = i
        self.Third = self.roster[indAcc]
        for i in range(4):
            if i != indAcc and i != indSmort and i != indSweep:
                self.Second = self.roster[i]
                break

