
from Sheet import *
from Linked_List_Curling import *
from Spot import *





def game(h, a, ends=10, stones=8, p=.5, playoff=False, neutral=False):  # Home, Away, Game Length, End Length, Print Value
    h.color = 'Blue'  # Home team is Blue, Away is Red
    a.color = 'Red'
    if neutral:
        if random.randrange(2) == 0:
            hammer = h
            lead = a
        else:
            hammer = a
            lead = h
    else:
        hammer = h  # Giving first hammer to home team for home field advantage
        lead = a
    firstHammer = hammer
    hScore = Linked_List()  # These three are for the scoreboard, if you run it and look at the scoreboard itll make more sense
    aScore = Linked_List()
    endCount = Linked_List()
    endNum = 1
    while endNum <= ends or hScore.sum() == aScore.sum():  # If still tied, go to extra ends.
        endCount.append_element(endNum)  # adds column to scoreboard
        if p > 1:
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
    hFinal = hScore.sum()
    aFinal = aScore.sum()
    hScore.append_element(hFinal)  # Final Scores
    aScore.append_element(aFinal)
    if p >= 1:  # Prints the scoreboard
        print(firstHammer.ABR, 'has the first hammer')
        print('Team Name    '+str(endCount))
        print(h.name, hScore)
        print(a.name, aScore)
    if p > 0 < 1:
        print(h.ABR, hFinal, aFinal, a.ABR)
    if playoff:
        if hFinal > aFinal:
            return h
        else:
            return a
    else:
        h.played += 1
        a.played += 1
        h.pD += hFinal
        h.pD -= aFinal
        a.pD += aFinal
        a.pD -= hFinal
        h.tPD += hFinal
        h.tPD -= aFinal
        a.tPD += aFinal
        a.tPD -= hFinal
        if hFinal > aFinal:
            h.wins += 1
            h.tWins += 1
        else:
            a.wins += 1
            a.tWins += 1


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
            xTar = float(input('Y Target:'))
            yTar = float(input('X Target:'))
            target = [xTar, yTar]
        else:
            target = spot(sheet, stones, lead.color, (2 * i) + 1)  # Computer Decision-Making
        sheet.shot(shooter, skip, sweep1, sweep2, hammer.color, target)  # Look okay it takes a lot of info
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
            xTar = float(input('Y Target:'))
            yTar = float(input('X Target:'))
            target = [xTar, yTar]
        else:
            target = spot(sheet, stones, lead.color, (2 * i) + 1)
        sheet.shot(shooter, skip, sweep1, sweep2, hammer.color, target)
        if p >= 2:
            sheet.output()
        #print(len(sheet.stones))
    if 1.5 <= p < 2:
        sheet.output()
    return sheet.score()  # Gives the team and score back to the game function
