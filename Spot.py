import random  # This is going to be a whole thing. Where the computer aims its shots.
import math
# return [vY, vX]

# Define values here so they can be adjusted everywhere in the code at once
split = .01  # in seconds, how often the movement updates
gravForce = 32.2  # g in feet
coefFriction = .02  # Frictional Coefficient
decel = gravForce * coefFriction * split  # how much v goes down every split
sweepMag = 0.1  # Adjustable multiplier for the magnitude of sweeping force


def pythag(x, y):  # It's just nice to have
    return math.sqrt(x ** 2 + y ** 2)


def targetReq(y, x, multiplier=1.):  # Turns X/Y coordinates into Velo components, option for multiplier if u wanna hit it hard
    distTotal = pythag(y, x)
    angTarget = math.atan(x/y)
    acceleration = gravForce * coefFriction
    initV = math.sqrt(distTotal*acceleration*2)
    return [multiplier*initV*math.cos(angTarget), multiplier*initV*math.sin(angTarget)]


def landing(vY, vX, iY=0, iX=0):
    if vY:
        angle = math.atan(vX/vY)
    else:
        angle = math.pi/2
    accelCoefY = -gravForce * coefFriction * math.cos(angle)  # Physics Physics Physics
    if vX >= 0:
        accelCoefX = -gravForce * coefFriction * math.sin(angle)
    else:
        accelCoefX = gravForce * coefFriction * math.sin(angle)
    timeToStop = vY / -accelCoefY
    depthFinal = .5 * accelCoefY * (timeToStop ** 2) + vY * timeToStop + iY
    widthFinal = .5 * accelCoefX * (timeToStop ** 2) + vX * timeToStop + iX
    return [depthFinal, widthFinal]


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
                return [126, 0]
            else:
                target = house[0]
                #print('Takeout!')
                step1 = targetReq(target.depth, target.width, 1.1)
                return landing(step1[0], step1[1])
        else:
            #print('blank')
            return [150, 0]  # Blank the end
    elif num/2 <= math.floor(stones//4):  # Early like maybe throw a guard here. I know it's weird.
        x = random.randrange(100)
        # print(x)
        if x < 50:  # Throw a guard
            #print('Guard!')
            if num % 2 == 1:  # Lead team, curling theory is they throw center guards
                return [random.uniform(105, 120), 0]  # Center Guard
            else:  # Hammer Team, corner guards
                return [random.uniform(105, 120), random.choice([random.uniform(-7, -3), random.uniform(3, 7)])]
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
            return [random.uniform(120, 132), random.choice([random.uniform(-6, -2), random.uniform(2, 6)])]
        else:
            target = house[0]
            # print('Takeout!')
            step1 = targetReq(target.depth, target.width, 1.1)
            return landing(step1[0], step1[1])
    else:
        #print('draw!')
        return [random.uniform(120, 132), random.uniform(-2, 2)]  # Draw center

# return [random.randrange(115, 135), random.randrange(-10, 11), 0]
