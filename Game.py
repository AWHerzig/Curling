
from Sheet import *
from Linked_List_Curling import *
from Spot import *


def game(h, a, ends=10, stones=8, p=1):  # Home, Away, Game Length, End Length, Print Value
    h.color = 'Blue'  # Home team is Blue, Away is Red
    a.color = 'Red'
    hammer = h  # Giving first hammer to home team for home field advantage
    lead = a
    hScore = Linked_List()  # These three are for the scoreboard, if you run it and look at the scoreboard itll make more sense
    aScore = Linked_List()
    endCount = Linked_List()
    endNum = 1
    while endNum <= ends or hScore.sum() == aScore.sum():  # If still tied, go to extra ends.
        endCount.append_element(endNum)  # adds column to scoreboard
        print('END', endNum)
        res = end(hammer, lead, stones, p)  # The end is actually played with this function call.
        if res[0] == 'Blue':  # If Blue Scored
            hScore.append_element(res[1])
            aScore.append_element(0)
            hammer = a
            lead = h
        elif res[0] == 'Red':  # If Red Scored
            aScore.append_element(res[1])
            hScore.append_element(0)
            hammer = h
            lead = a
        else:  # Blank End
            hScore.append_element(0)
            aScore.append_element(0)
        endNum += 1
    endCount.append_element('T')
    hScore.append_element(hScore.sum())  # Final Scores
    aScore.append_element(aScore.sum())
    if p >= 1:  # Prints the scoreboard
        print('Team Name '+str(endCount))
        print(h.name, hScore)
        print(a.name, aScore)


def end(hammer, lead, stones, p):  # Hammer Color, Lead Color, Stones per team Print value
    sheet = Sheet()  # Object from Sheet file. Everything that happens on the sheet is represented here.
    for i in range(stones):
        #print(i+1, 'A')
        if i < stones * .25:  # In case it's not a base 4 number of stones per end
            shooter = lead.Lead
            skip = lead.Skip  # skip for the individual shot, not The Skip of the team, though they are the same unless Skip is shooting
            sweep1 = lead.Second  # Sweep1 is on the left, Sweep2 is on the right
            sweep2 = lead.Third
        elif i < stones * .5:
            shooter = lead.Second
            skip = lead.Skip
            sweep1 = lead.Third
            sweep2 = lead.Lead
        elif i < stones * .75:
            shooter = lead.Third
            skip = lead.Skip
            sweep1 = lead.Lead
            sweep2 = lead.Second
        else:
            shooter = lead.Skip
            skip = lead.Third
            sweep1 = lead.Lead
            sweep2 = lead.Second
        if shooter.controlled:  # User input for their players shot, in v2 they put in a Y and X Velocity
            # I am going to build in an option to use Depth and Width inputs and convert using the targetReq() function
            sheet.output()  # Lets the user see what's up so they can decide where to shoot
            cVeloY = float(input('Y Velocity:'))
            cVeloX = float(input('X Velocity:'))
            target = [cVeloY, cVeloX]
        else:
            target = spot(sheet, stones, lead.color, (2 * i) + 1)  # Computer Decision-Making
        sheet.shot(shooter, skip, sweep1, sweep2, hammer.color, target[0], target[1])  # Look okay it takes a lot of info
        if p >= 2:
            sheet.output()  # This is for very close watching
        #print(i+1, 'B')
        if i < stones * .25:  # All same but for team going second, the hammer team
            shooter = hammer.Lead
            skip = hammer.Skip
            sweep1 = hammer.Second
            sweep2 = hammer.Third
        elif i < stones * .5:
            shooter = hammer.Second
            skip = hammer.Skip
            sweep1 = hammer.Third
            sweep2 = hammer.Lead
        elif i < stones * .75:
            shooter = hammer.Third
            skip = hammer.Skip
            sweep1 = hammer.Lead
            sweep2 = hammer.Second
        else:
            shooter = hammer.Skip
            skip = hammer.Third
            sweep1 = hammer.Lead
            sweep2 = hammer.Second
        if shooter.controlled:
            sheet.output()
            cVeloY = float(input('Y Velo:'))
            cVeloX = float(input('X Velo:'))
            target = [cVeloY, cVeloX]
        else:
            target = spot(sheet, stones, lead.color, (2 * i) + 1)
        sheet.shot(shooter, skip, sweep1, sweep2, hammer.color, target[0], target[1])
        if p >= 2:
            sheet.output()
        #print(len(sheet.stones))
    if 1.5 <= p < 2:
        sheet.output()
    return sheet.score()  # Gives the team and score back to the game function
