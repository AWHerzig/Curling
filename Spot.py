import random  # This is going to be a whole thing. Where the computer aims its shots.
import math
# return [vY, vX]
from Sheet import gravForce, coefFriction, pythag


def targetReq(y, x, multiplier=1.1):  # Turns X/Y coordinates into Velo components, option for multiplier if u wanna hit it hard
    distTotal = pythag(y, x)
    angTarget = math.atan(x/y)
    acceleration = gravForce * coefFriction
    initV = math.sqrt(distTotal*acceleration*2)
    return [multiplier*initV*math.cos(angTarget), multiplier*initV*math.sin(angTarget)]


def spot(sheet, stones, color, num):  # num is this specific stone, stones is number of stones per team*end
    if num == stones * 2:  # Hammer
        # sheet.output()
        sheet.scoreSort(sheet.stones)  # In the order that they would score
        point = 0  # this next bit is about trying to get an array of just in the house, which i might use later
        for i in sheet.stones:
            if i.dist > 6.5:
                point = sheet.stones.index(i)
                break
        if point == 0 and len(sheet.stones) > 0:  # If all stones in the house it used to treat it as no stones
            point = len(sheet.stones) - 1
        #print(point)
        if point != 0:
            house = sheet.stones.copy()[0:point]
            if house[0].color == color:
                #print('button!')
                return targetReq(126, 0, 1)
            else:
                target = house[0]
                #print('Takeout!')
                return targetReq(target.depth, target.width)
        else:
            #print('blank')
            return [150, 0]  # Blank the end
    elif num/2 <= math.floor(stones//4):  # Early like maybe throw a guard here. I know it's weird.
        x = random.randrange(100)
        # print(x)
        if x < 50:  # Throw a guard
            #print('Guard!')
            if num % 2 == 1:  # Lead team, curling theory is they throw center guards
                return [random.uniform(11.75, 12.5), 0]  # Center Guard
            else:  # Hammer Team, corner guards
                return [random.uniform(11.75, 12.75), random.choice([random.uniform(-.5, -.1), random.uniform(.1, .5)])]
    point = 0
    for i in sheet.stones:
        if i.dist > 6.5:
            point = sheet.stones.index(i)
            break
    if point == 0 and len(sheet.stones):
        point = len(sheet.stones) - 1
    if point != 0:
        house = sheet.stones.copy()[0:point]
        if house[0].color == color:
            #print('draw!')
            return [random.uniform(12.5, 13), random.choice([random.uniform(-.4, -.1), random.uniform(.1, .4)])]
        else:
            #print('takeout')
            target = house[0]
            return targetReq(target.depth, target.width)
    else:
        #print('draw!')
        return [random.uniform(12.5, 13), random.uniform(-.1, .1)]  # Draw center

# return [random.randrange(115, 135), random.randrange(-10, 11), 0]
