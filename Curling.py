# So it's curling right
# 120 ft (distance is going to be feet) from shot to front of house.
# House is 12 feet deep and perfect circle.
# 20 ft across actually maybe it's 19, irl it's 16.5 i think
# Hog line at 105ft, T at 135 i think is where i put it even though i think technically is might be 132
# Players will have x-acc, y-acc, sweep, and *maybe* brains
# Teams have Leads, Seconds, Thirds and Skips
# Stones are assumed to be 1ft in diameter, irl it's 11in


from Game import *  # Allows Everything (that's the *) from Game.py to be used here.
from Sheet import *


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
            else:
                rando = random.randrange(100)  # I really don't know where to go with this decision making
                if rando < 25:
                    return 0  # Don't Sweep
                elif rando < 50:
                    return 1  # Sweep it to the side
                elif rando < 75:
                    return 2  # Sweep ahead to speed up
                else:
                    return 3  # Lil o both
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
        self.Lead = Player(names.get_full_name())  # names is a library of names you can pull from so u dont have to make them up
        self.Second = Player(names.get_full_name())  # Have plans to reorder these so better players more likely to be skip
        self.Third = Player(names.get_full_name())
        self.Skip = Player(names.get_full_name())
        self.roster = [self.Lead, self.Second, self.Third, self.Skip]
        self.color = None  # Will be 'Blue' or 'Red' assigned at each game

# HERE DOWN IS ACTUAL RUNNING OF THE CODE NOT JUST WRITING FUNCTIONS.


A = Team('Team Blue', 'BLU')
# A.Skip.controlled = True
B = Team('Team Red ', 'RED')
game(A, B, p=1.5, ends=10)
