import math  # This file is where the shit gets real
import numpy
import random
import names
from Spot import *



def pythag(x, y):  # It's just nice to have
    return math.sqrt(x ** 2 + y ** 2)


class Sheet:  # This will store what happens on the sheet in any end
    class Stone:  # I feel like this one is more self-explanatory
        def __init__(self, color, vY, vX, target):
            self.ID = names.get_first_name('Male') + color
            self.depth = 0  # Depth and Width are now where it is (used to be where it was going)
            self.width = 0
            self.color = color  # 'Blue' or 'Red'
            self.vY = vY
            self.vX = vX
            self.target = target
            if self.vY:
                self.angle = math.atan(self.vX / self.vY)  # All angles are with respect to vertical
            else:
                self.angle = math.pi/2
            self.dist = pythag(126 - self.depth, self.width)  # Distance from button
            if color == 'Red':  # Gets shown on the output of the sheet
                self.char = 'r'  # Will get capitalized if it's in the house
            else:
                self.char = 'b'

        def jump(self, dist):  # Jumps the movement ahead to a certain distance. Used to save processor time pre hog line when you KNOW it wont hit anything
            accelCoef = -gravForce * coefFriction * math.cos(self.angle)  # Acceleration in Y
            if (self.vY ** 2) < (2 * accelCoef * -dist):  # It's not gonna make the dist before stopping
                return False  # kill it
            timeToDist = (-self.vY + math.sqrt((self.vY ** 2) - (2 * accelCoef * -dist))) / accelCoef  # Quadraaaaaatic formula
            self.depth = dist
            self.width = -.5 * gravForce * coefFriction * math.sin(self.angle) * (timeToDist ** 2) + self.vX * timeToDist  # change in y = .5at^2 + vt
            self.vX -= gravForce * coefFriction * timeToDist * math.sin(self.angle)  # change in v = at
            self.vY -= gravForce * coefFriction * timeToDist * math.cos(self.angle)
            return True  # just cuz i guess

        def path(self):  # Tells where a stone will naturally stop
            accelCoefY = -gravForce * coefFriction * math.cos(self.angle)  # Physics Physics Physics
            if self.vX >= 0:
                accelCoefX = -gravForce * coefFriction * math.sin(self.angle)
            else:
                accelCoefX = gravForce * coefFriction * math.sin(self.angle)
            timeToStop = self.vY / -accelCoefY
            depthFinal = .5*accelCoefY*(timeToStop**2) + self.vY*timeToStop + self.depth
            widthFinal = .5*accelCoefX*(timeToStop**2) + self.vX*timeToStop + self.width
            return [depthFinal, widthFinal]

    def __init__(self):
        self.stones = []  # Stores all stones in play
        self.movers = []  # Keeps track of what's all moving
        self.blacklist = []  # Stones that already hit arent allowed to hit again on the same shot
        self.table = [None] * 8  # Output map
        self.stopwatch = 0  # Helpful for debugging and whatnot
        self.sheetReset()  # sets up the output table

    def sheetReset(self):
        self.depthSort(self.stones)
        for i in range(8):
            self.table[i] = [' '] * 21  # So that first index was depth range, this establishes the width
            self.table[i][0] = '|'  # Edge Lines
            self.table[i][20] = '|'  # Edge Lines
        self.table[3][10] = '*'  # Button
        self.table[0][10] = '_'  # These are roundabouts the outer circle but not exactly but roundabouts
        self.table[5][10] = '_'
        self.table[3][3] = '|'
        self.table[3][17] = '|'
        for i in self.stones:
            val = math.floor((i.depth - 115) / 2.5)
            if 0 < val <= 7:
                if self.table[7 - val][int(i.width) + 10] not in 'rbRB':
                    self.table[7 - val][int(i.width) + 10] = i.char  # Each Stone gets represented somewhere
                else:
                    self.table[7 - val][int(i.width) + 10] += i.char  # I might come back and change this but for now...

    def depthSort(self, group):  # It's insertion sort, sorts them in ascending order of depth.
        for k in range(len(group)):
            minloc = k
            j = k + 1
            while j < len(group):
                if group[j].depth < group[minloc].depth:  # This is the key line.
                    minloc = j
                j = j + 1
            cur = group[minloc]
            group[minloc] = group[k]
            group[k] = cur

    def scoreSort(self, group):  # It still is, now in order of scoring
        for i in group:
            i.dist = pythag(126 - i.depth, i.width)
        for k in range(len(group)):
            minloc = k
            j = k + 1
            while j < len(group):
                if group[j].dist < group[minloc].dist:
                    minloc = j
                j = j + 1
            cur = group[minloc]
            group[minloc] = group[k]
            group[k] = cur

    def output(self):
        self.sheetReset()
        for i in self.table:
            print(i[0] + i[1] + i[2] + i[3] + i[4] + i[5] + i[6] + i[7] + i[8] + i[9] + i[10]
                  + i[11] + i[12] + i[13] + i[14] + i[15] + i[16] + i[17] + i[18] + i[19] + i[20])
        for i in self.stones:
            if i.depth <= 135:  # Currently this is everything, originally it was just going to be for guards.
                print(i.color, 'stone at', round(i.depth, 2), 'depth and', round(i.width, 2), 'width for',
                      round(i.dist, 2), 'distance from button.')

    def shot(self, shooter, skip, sweep1, sweep2, color, target):  # Depth and Width are where it's going not where it is
        odds = random.randrange(100)  # Random numer 1-100
        odds2 = random.randrange(100)
        V = targetReq(target[0], target[1])
        vY = V[0]
        vX = V[1]
        if odds < .3*((shooter.xAcc - 5)**3) + 50:  # See if they missed in the x-direction
            vX += numpy.random.normal(0, 1)
        if odds2 < .3*((shooter.xAcc - 5)**3) + 50:  # See if they missed in the y-direction
            vY += numpy.random.normal(0, 3)
        rock = self.Stone(color, vY, vX, target)  # Build the stone, toiling for days mining the mountains of Alisa Craig, Scotland, for only the finest granite. Polishing it until it shines brighter than a city at night. Ship it across the world, into whatever computer this runs on, and get it in position to be shot.
        #for i in range(10, 90, 20):
         #   whoop = rock.jump(i)
          #  if not whoop:
           #     return
            #self.sweepOp(rock, skip, sweep1, sweep2)
        whoop2 = rock.jump(104.5)  # didn't have a good variable name, saves time by skipping up to the hog line
        if not whoop2:
            return
        self.stones.append(rock)  # If you clear the hog line you get added to the list of stones, good for you!
        self.movers.append(rock)  # and its still moving so u get added here too
        moving = True  # True as long as *something* is moving
        self.stopwatch = 0  # These two have to be reset with each shot
        self.blacklist = []
        while moving:  # If everything is still, moving will return as false, and the shot will end.
            moving = self.movement()

    def sweepOp(self, rock, skip, sweep1, sweep2):  # CURRENTLY NOT IN USE CUZ... I DUNNO BUT ITS BAD
        rando = random.randrange(100)
        if rando < 100 * math.log(skip.smart, 10) or rando < 100 * math.log(sweep1.smart, 10):
            lefty = sweep1.sweepDec(rock, True, 'decrease')
        else:
            lefty = sweep1.sweepDec(rock, False, 'decrease')
        if rando < 100 * math.log(skip.smart, 10) or rando < 100 * math.log(sweep2.smart, 10):
            righty = sweep2.sweepDec(rock, True, 'increase')
        else:
            righty = sweep2.sweepDec(rock, False, 'increase')
        if lefty == 1:
            rock.vX -= sweepMag * math.sqrt(sweep1.sweep)
        elif lefty == 2:
            rock.vY += sweepMag * math.sqrt(sweep1.sweep)
        elif lefty == 3:
            rock.vX -= sweepMag * math.sqrt(sweep1.sweep) * math.sqrt(2) * .5
            rock.vY += sweepMag * math.sqrt(sweep1.sweep) * math.sqrt(2) * .5
        if righty == 1:
            rock.vX += sweepMag * math.sqrt(sweep2.sweep)
        elif righty == 2:
            rock.vY += sweepMag * math.sqrt(sweep2.sweep)
        elif righty == 3:
            rock.vX += sweepMag * math.sqrt(sweep2.sweep) * math.sqrt(2) * .5
            rock.vY += sweepMag * math.sqrt(sweep2.sweep) * math.sqrt(2) * .5

    def movement(self):  # Okay I don't even understand half of this
        for i in self.movers:  # First, we move everything
            i.depth += (-.5 * decel * math.cos(i.angle) * split) + (split * i.vY)  # change in position
            i.width += (-.5 * decel * math.sin(i.angle) * split) + (split * i.vX)
            i.vY -= decel * math.cos(i.angle)  # change in velocity
            #i.vY = max(i.vY, 0)
            i.vX -= decel * math.sin(i.angle)
            #i.vX = max(i.vX, 0)
            #print(i.ID, i.vY, i.vX, i.depth, i.width)
            if -.1 < i.vY < .1:  # I hate floats and everything they stand for, these are trying to nip that in the bud
                i.vY = 0
            if -.1 < i.vX < .1:
                i.vX = 0
        self.stopwatch += split  # Timer increment
        for i in self.movers:  # Second, check for collisions
            for j in self.stones:  # it can hit any stone, not just those that are moving
                breaker = False
                for b in self.blacklist:  # Objects in here are in pairs
                    if (b[0] == i and b[1] == j) or (b[0] == j and b[1] == i):  # So they can go both ways, gotta check both
                        breaker = True
                if i != j and not breaker:  # If not itself and does not need to break
                    dDiff = j.depth - i.depth  # Difference between depths
                    wDiff = j.width - i.width  # Difference between widths
                    tDiff = pythag(wDiff, dDiff)  # total Difference in distance
                    if tDiff <= 1:  # they hit
                        #print('Contact!', round(tDiff, 2), round(dDiff, 2), round(wDiff, 2), round(self.stopwatch, 3))
                        #print('i:', i.ID, round(i.depth), round(i.width), round(i.vY, 2), round(i.vX, 2))
                        #print('j:', j.ID, round(j.depth), round(j.width), round(j.vY, 2), round(j.vX, 2))
                        self.blacklist.append([j, i])  # If they hit they can't hit again
                        self.blacklist.append([i, j])  # Technically I only need one, but what the hell
                        dDiff = dDiff / tDiff  # Bring back the stone, so they're just touching not actual overlap
                        wDiff = wDiff / tDiff  # These first two are scaling the distances so the centers are 1ft away
                        i.depth = j.depth - dDiff  # Respot it, this should be a very small change
                        i.width = j.width - wDiff  # same
                        vTy = i.vY + j.vY  # Total Y velocity
                        vTx = round(i.vX + j.vX, 2)  # Needs to be rounded cuz again floats suck and I hate them
                        # From here, v is velo, x/y is direction, 1 means post collision, i/j is the stone
                        if wDiff == 0:  # Case 1: Head on. A lot of math revolves around dDiff/wDiff, so no DivBy0
                            vx1j = j.vX  # j.vX constant
                            vx1i = i.vX  # i.vX constant
                            vy1j = i.vY  # Flip em!
                            vy1i = j.vY
                        elif j.vY == 0 and j.vX == 0:  # Case dos: j is still
                            if dDiff == 0:  # DivByZero kind of thing
                                vy1j = 0
                                vx1j = i.vX
                                vy1i = i.vY
                                vx1i = 0
                            else:
                                t1 = wDiff / dDiff
                                vy1j = (i.vY + (t1 * i.vX)) / ((t1**2) + 1)  # Source: Trust me bro
                                vx1j = t1 * vy1j
                                vy1i = i.vY - vy1j
                                vx1i = i.vX - vx1j
                        else:  # Case 3: both moving
                            t1 = dDiff / wDiff
                            t2 = (i.vY * j.vY) + (i.vX * j.vX)  # bro
                            t3 = (t1 * j.vX) + i.vY  # just...
                            t4 = -(t1 ** 2 + 1)
                            t5 = (2*t3*t1) - (vTy * t1) + vTx  # just trust me bro
                            t6 = (vTy*i.vY) + (vTy*j.vX*t1) - (t3**2) - t2  # I know I know
                            if 4 * t4 * t6 > t5 ** 2:  # I think I fixed all of these but its here for debugs
                                print('stahp')
                            vx1j = (-t5 - math.sqrt((t5 ** 2) - (4 * t4 * t6))) / (2 * t4)  # This is plus or minus so... i dunno
                            # TRUST ME BRO
                            if abs(vx1j) < .1:  # I don't even know if this is still necessary
                                vx1j = 0
                            vx1i = vTx - vx1j  # Conservation of x momentum
                            if abs(vx1i) < .1:
                                vx1i = 0
                            vy1i = i.vY - (t1 * (vx1j - j.vX))  # I actually just spammed by keyboard and this popped up so I went with it
                            if abs(vy1i) < .1:
                                vy1i = 0
                            vy1j = vTy - vy1i  # conservation of y momentum
                            if abs(vy1j) < .1:
                                vy1j = 0
                            if j.vX == vx1j:  # Case 2 before case 2 was case 2 but figured I'd leave it in just in case
                                vy1j = i.vY
                                vy1i = j.vY
                        i.vY = vy1i  # Now apply the new values, recalc the angles
                        j.vY = vy1j
                        i.vX = vx1i
                        j.vX = vx1j
                        if i.vY:
                            i.angle = math.atan(i.vX/i.vY)
                        else:
                            i.angle = 0
                        if j.vY:
                            j.angle = math.atan(j.vX/j.vY)
                        else:
                            j.angle = 0
                        #print(round(i.vY, 2), round(i.vX, 2), round(j.vY, 2), round(j.vX, 2))
                        if j not in self.movers:  # If j wasn't moving before it is now.
                            self.movers.append(j)
        for i in self.movers:  # Step 3, checks
            # print(i.vY, i.vX)
            if i.vY == 0 and i.vX == 0:  # if it stopped moving
                #print(i.ID, i.depth, i.width)
                self.movers.remove(i)
            if i.depth > 135 or i.width < -10 or i.width > 10:  # If it's gone out of bounds
                if i in self.movers:
                    self.movers.remove(i)
                self.stones.remove(i)
        if len(self.movers) == 0:  # If nothing is still moving
            for i in self.stones:
                if i.depth < 105:  # If anything ended up short of the hog line, lose it
                    self.stones.remove(i)
                i.dist = pythag(126 - i.depth, i.width)  # Update distances from button
                if i.dist <= 6.5:  # Cuz it just has to touch
                    i.char = i.char.capitalize()  # This is how we mark it's in the house
                else:
                    i.char = i.char.lower()  # This is out of the house
            return False  # Shot is over
        else:
            return True  # We need to call this movement function again. Things still in motion.

    def score(self):  # Scoring the sheet, called at the end's end
        self.scoreSort(self.stones)  # Get them in order
        self.stones.append(self.Stone('BLANK', 0, 0, [0, 0]))  # Put a blank at the end so the whole thing doesn't fritz out if there are no stones in play
        if self.stones[0].dist <= 6.5:  # If anything is in the house
            lead = self.stones[0]
            leadColor = lead.color  # Which team will get points
            score = 1
            while self.stones[score].color == leadColor and self.stones[score].dist <= 6.5:
                score += 1  # 1 point for all of leadColor before first other color.
                # Fancy lil trick here, the number of points increments evenly with index of the stone we need to see
            return [leadColor, score]  # [Team that scored, How much they scored]
        else:  # Blank End
            return ['BLANK', 0]
