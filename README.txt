Herzig Curling v2(.1ish), will be changing a lot in the near future.

This file comes to you in 2 parts. Part 1 is an explanation of the game of curling, part 2 is a rough description of each file in the repository.

Part 1 - Rules of Curling.
Curling is a "gentleman's game" between 2 teams of 4 players. The teams alternating pushing (often called "throwing") stones across a sheet of ice ("the sheet") toward a target ("the house").
Games are separated into distinct "ends", which can basically be thought of as "innings", although both teams play at the same time, rather than a top and bottom.
Standard length games are 10 ends, with each team throwing 8 stones in each end.
Stones that lie at rest short of the Hog Line are removed, as well as those that are past the T Line in the back.
To score points, at the end's end, the closest stone to the button (center of the house), is worth one point, so long as it lies within the house.
In order of distance from the button (and only counting those in the house) additional stones of the same color before the first stone are also worth one point.
Thus, only 1 team can score in any given end. (unless there are no stones in the house in which neither scores in a "blank" end)
It is a huge advantage to go second in any end, and is called having "the hammer".
The team that does not score in each end gets the hammer in the next end. After blank ends, the team with the hammer keeps it.
There are different kinds of shots including guards, takeouts, draws, and freezes, you can look them up if you really care enough to know
The 4 players each have a title, referring to the order in which they take shots.
    The "Lead" takes the first 2, generally throwing guards and draws
    The "Second" takes the next 2
    The "Third" takes 5 and 6, and is generally second-in-command
    The "Skip" takes the final 2, and is the captain of the team. IRL, the Skip has final decisions on where each shot is aimed.
That's all I can think of right now. Of course, questions are welcome and there's always google.

Part 2 - Outline of repository.
Curling.py - This is the main file. When running the program, RUN THIS ONE. Player and Team Object Classes are defined here, and the whole actually telling the code what you want from it thing, instead of just defining functions.
Game.py - Here is defined the shell of the game and each end. Just the basics
Sheet.py - This one does the heavy lifting on the weird shit. Everything that happens on the sheet.
Spot.py - How the computer decides to aim to its shots
Linked_List_Curling.py - A modified version of a project from W&M CSCI241, works well for scoreboard values.
CurlingOutPut.py - NOTHING. Eventually it will hopefully be where I learn how to use PyGame or some shit and make this look nice instead of how it is now.

I lied there's a part 3 - Future plans
v2.1 will have differing player skills and sweeping
v3 will have some actual game mode to this, some kind of league cuz I think it would be funny and makes it interesting. Personal player progression and full team control in Tournaments
vAtSomePoint will have player stats and data shit and I'm gonna try to learn R.
vEventually will hopefully have good output
I made up the v's to sound cooler

Go wild. Questions are welcome. Ideas are also welcome.