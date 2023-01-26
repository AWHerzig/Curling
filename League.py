from PlayerTeam import *
from Game import *
import pandas as pd
# League info will go here


# Teams
NAteams = [
    Team('Toronto     ', 'TOR'),
    Team('Mexico City ', 'MEX'),
    Team('New York    ', 'NYC'),
    Team('Los Angeles ', 'LA '),
    Team('Washington  ', 'DC ')
]
SAteams = [
    Team('Buenos Aires', 'BA '),
    Team('Santiago    ', 'SAN'),
    Team('Montevideo  ', 'MON'),
    Team('Rio-Janeiro ', 'RdJ'),
    Team('Caracas     ', 'CAR')
]
WEteams = [
    Team('London      ', 'LON'),
    Team('Paris       ', 'PAR'),
    Team('Madrid      ', 'MAD'),
    Team('Rome        ', 'ROM'),
    Team('Lisbon      ', 'LIS')
]
EEteams = [
    Team('Warsaw      ', 'WAR'),
    Team('Moscow      ', 'MOS'),
    Team('Helsinki    ', 'HEL'),
    Team('Kyiv        ', 'KYV'),
    Team('Prague      ', 'PRA')
]
AFteams = [
    Team('Cairo       ', 'CAI'),
    Team('Lagos       ', 'LAG'),
    Team('Johannesburg', 'JBG'),
    Team('Kinshasa    ', 'KIN'),
    Team('Nairobi     ', 'NAI')
]
OCteams = [
    Team('Sydney      ', 'SYD'),
    Team('Auckland    ', 'AUC'),
    Team('Melbourne   ', 'MEL'),
    Team('Jakarta     ', 'JAK'),
    Team('Manila      ', 'MAN')
]
WAteams = [
    Team('Istanbul    ', 'IST'),
    Team('Tehran      ', 'TEH'),
    Team('Jerusalem   ', 'JER'),
    Team('New Delhi   ', 'ND '),
    Team('Islamabad   ', 'ISL')
]
EAteams = [
    Team('Beijing     ', 'BEI'),
    Team('Seoul       ', 'SEO'),
    Team('Tokyo       ', 'TOK'),
    Team('Taipei      ', 'TAI'),
    Team('Shanghai    ', 'SHA')
]


class League:
    def __init__(self):
        self.NA = pd.DataFrame({
            'Team': [NAteams[0], NAteams[1], NAteams[2], NAteams[3], NAteams[4]],
            'ABR ': [NAteams[0].ABR, NAteams[1].ABR, NAteams[2].ABR, NAteams[3].ABR, NAteams[4].ABR],
            'Played': [NAteams[0].played, NAteams[1].played, NAteams[2].played, NAteams[3].played, NAteams[4].played],
            'Stage Wins': [NAteams[0].wins, NAteams[1].wins, NAteams[2].wins, NAteams[3].wins, NAteams[4].wins],
            'Stage PD': [NAteams[0].pD, NAteams[1].pD, NAteams[2].pD, NAteams[3].pD, NAteams[4].pD],
            'Season Wins': [NAteams[0].tWins, NAteams[1].tWins, NAteams[2].tWins, NAteams[3].tWins, NAteams[4].tWins],
            'Season PD': [NAteams[0].tPD, NAteams[1].tPD, NAteams[2].tPD, NAteams[3].tPD, NAteams[4].tPD]
        })
        self.SA = pd.DataFrame({
            'Team': [SAteams[0], SAteams[1], SAteams[2], SAteams[3], SAteams[4]],
            'ABR ': [SAteams[0].ABR, SAteams[1].ABR, SAteams[2].ABR, SAteams[3].ABR, SAteams[4].ABR],
            'Played': [SAteams[0].played, SAteams[1].played, SAteams[2].played, SAteams[3].played, SAteams[4].played],
            'Stage Wins': [SAteams[0].wins, SAteams[1].wins, SAteams[2].wins, SAteams[3].wins, SAteams[4].wins],
            'Stage PD': [SAteams[0].pD, SAteams[1].pD, SAteams[2].pD, SAteams[3].pD, SAteams[4].pD],
            'Season Wins': [SAteams[0].tWins, SAteams[1].tWins, SAteams[2].tWins, SAteams[3].tWins, SAteams[4].tWins],
            'Season PD': [SAteams[0].tPD, SAteams[1].tPD, SAteams[2].tPD, SAteams[3].tPD, SAteams[4].tPD]

        })
        self.WE = pd.DataFrame({
            'Team': [WEteams[0], WEteams[1], WEteams[2], WEteams[3], WEteams[4]],
            'ABR ': [WEteams[0].ABR, WEteams[1].ABR, WEteams[2].ABR, WEteams[3].ABR, WEteams[4].ABR],
            'Played': [WEteams[0].played, WEteams[1].played, WEteams[2].played, WEteams[3].played, WEteams[4].played],
            'Stage Wins': [WEteams[0].wins, WEteams[1].wins, WEteams[2].wins, WEteams[3].wins, WEteams[4].wins],
            'Stage PD': [WEteams[0].pD, WEteams[1].pD, WEteams[2].pD, WEteams[3].pD, WEteams[4].pD],
            'Season Wins': [WEteams[0].tWins, WEteams[1].tWins, WEteams[2].tWins, WEteams[3].tWins, WEteams[4].tWins],
            'Season PD': [WEteams[0].tPD, WEteams[1].tPD, WEteams[2].tPD, WEteams[3].tPD, WEteams[4].tPD]
        })
        self.EE = pd.DataFrame({
            'Team': [EEteams[0], EEteams[1], EEteams[2], EEteams[3], EEteams[4]],
            'ABR ': [EEteams[0].ABR, EEteams[1].ABR, EEteams[2].ABR, EEteams[3].ABR, EEteams[4].ABR],
            'Played': [EEteams[0].played, EEteams[1].played, EEteams[2].played, EEteams[3].played, EEteams[4].played],
            'Stage Wins': [EEteams[0].wins, EEteams[1].wins, EEteams[2].wins, EEteams[3].wins, EEteams[4].wins],
            'Stage PD': [EEteams[0].pD, EEteams[1].pD, EEteams[2].pD, EEteams[3].pD, EEteams[4].pD],
            'Season Wins': [EEteams[0].tWins, EEteams[1].tWins, EEteams[2].tWins, EEteams[3].tWins, EEteams[4].tWins],
            'Season PD': [EEteams[0].tPD, EEteams[1].tPD, EEteams[2].tPD, EEteams[3].tPD, EEteams[4].tPD]
        })
        self.AF = pd.DataFrame({
            'Team': [AFteams[0], AFteams[1], AFteams[2], AFteams[3], AFteams[4]],
            'ABR ': [AFteams[0].ABR, AFteams[1].ABR, AFteams[2].ABR, AFteams[3].ABR, AFteams[4].ABR],
            'Played': [AFteams[0].played, AFteams[1].played, AFteams[2].played, AFteams[3].played, AFteams[4].played],
            'Stage Wins': [AFteams[0].wins, AFteams[1].wins, AFteams[2].wins, AFteams[3].wins, AFteams[4].wins],
            'Stage PD': [AFteams[0].pD, AFteams[1].pD, AFteams[2].pD, AFteams[3].pD, AFteams[4].pD],
            'Season Wins': [AFteams[0].tWins, AFteams[1].tWins, AFteams[2].tWins, AFteams[3].tWins, AFteams[4].tWins],
            'Season PD': [AFteams[0].tPD, AFteams[1].tPD, AFteams[2].tPD, AFteams[3].tPD, AFteams[4].tPD]
        })
        self.OC = pd.DataFrame({
            'Team': [OCteams[0], OCteams[1], OCteams[2], OCteams[3], OCteams[4]],
            'ABR ': [OCteams[0].ABR, OCteams[1].ABR, OCteams[2].ABR, OCteams[3].ABR, OCteams[4].ABR],
            'Played': [OCteams[0].played, OCteams[1].played, OCteams[2].played, OCteams[3].played, OCteams[4].played],
            'Stage Wins': [OCteams[0].wins, OCteams[1].wins, OCteams[2].wins, OCteams[3].wins, OCteams[4].wins],
            'Stage PD': [OCteams[0].pD, OCteams[1].pD, OCteams[2].pD, OCteams[3].pD, OCteams[4].pD],
            'Season Wins': [OCteams[0].tWins, OCteams[1].tWins, OCteams[2].tWins, OCteams[3].tWins, OCteams[4].tWins],
            'Season PD': [OCteams[0].tPD, OCteams[1].tPD, OCteams[2].tPD, OCteams[3].tPD, OCteams[4].tPD]
        })
        self.WA = pd.DataFrame({
            'Team': [WAteams[0], WAteams[1], WAteams[2], WAteams[3], WAteams[4]],
            'ABR ': [WAteams[0].ABR, WAteams[1].ABR, WAteams[2].ABR, WAteams[3].ABR, WAteams[4].ABR],
            'Played': [WAteams[0].played, WAteams[1].played, WAteams[2].played, WAteams[3].played, WAteams[4].played],
            'Stage Wins': [WAteams[0].wins, WAteams[1].wins, WAteams[2].wins, WAteams[3].wins, WAteams[4].wins],
            'Stage PD': [WAteams[0].pD, WAteams[1].pD, WAteams[2].pD, WAteams[3].pD, WAteams[4].pD],
            'Season Wins': [WAteams[0].tWins, WAteams[1].tWins, WAteams[2].tWins, WAteams[3].tWins, WAteams[4].tWins],
            'Season PD': [WAteams[0].tPD, WAteams[1].tPD, WAteams[2].tPD, WAteams[3].tPD, WAteams[4].tPD]
        })
        self.EA = pd.DataFrame({
            'Team': [EAteams[0], EAteams[1], EAteams[2], EAteams[3], EAteams[4]],
            'ABR ': [EAteams[0].ABR, EAteams[1].ABR, EAteams[2].ABR, EAteams[3].ABR, EAteams[4].ABR],
            'Played': [EAteams[0].played, EAteams[1].played, EAteams[2].played, EAteams[3].played, EAteams[4].played],
            'Stage Wins': [EAteams[0].wins, EAteams[1].wins, EAteams[2].wins, EAteams[3].wins, EAteams[4].wins],
            'Stage PD': [EAteams[0].pD, EAteams[1].pD, EAteams[2].pD, EAteams[3].pD, EAteams[4].pD],
            'Season Wins': [EAteams[0].tWins, EAteams[1].tWins, EAteams[2].tWins, EAteams[3].tWins, EAteams[4].tWins],
            'Season PD': [EAteams[0].tPD, EAteams[1].tPD, EAteams[2].tPD, EAteams[3].tPD, EAteams[4].tPD]
        })
        self.Divisions = [self.NA, self.SA, self.WE, self.EE, self.AF, self.OC, self.WA, self.EA]
        self.Cities = ['New York', 'Los Angeles', 'Mexico City', 'Toronto', 'Washington DC',
                       'Buenos Aires', 'Santiago', 'Montevideo', 'Rio de Janeiro', 'Caracas',
                       'London', 'Paris', 'Madrid', 'Rome', 'Lisbon',
                       'Warsaw', 'Moscow', 'Helsinki', 'Kyiv', 'Prague',
                       'Cairo', 'Lagos', 'Johannesburg', 'Kinshasa', 'Nairobi',
                       'Sydney', 'Auckland', 'Melbourne', 'Jakarta', 'Manila',
                       'Istanbul', 'Tehran', 'Jerusalem', 'New Delhi', 'Islamabad',
                       'Beijing', 'Seoul', 'Tokyo', 'Taipei', 'Shanghai']

    def tableRefresh(self):
        self.NA = pd.DataFrame({
            'Team': [NAteams[0], NAteams[1], NAteams[2], NAteams[3], NAteams[4]],
            'ABR ': [NAteams[0].ABR, NAteams[1].ABR, NAteams[2].ABR, NAteams[3].ABR, NAteams[4].ABR],
            'Played': [NAteams[0].played, NAteams[1].played, NAteams[2].played, NAteams[3].played, NAteams[4].played],
            'Stage Wins': [NAteams[0].wins, NAteams[1].wins, NAteams[2].wins, NAteams[3].wins, NAteams[4].wins],
            'Stage PD': [NAteams[0].pD, NAteams[1].pD, NAteams[2].pD, NAteams[3].pD, NAteams[4].pD],
            'Season Wins': [NAteams[0].tWins, NAteams[1].tWins, NAteams[2].tWins, NAteams[3].tWins, NAteams[4].tWins],
            'Season PD': [NAteams[0].tPD, NAteams[1].tPD, NAteams[2].tPD, NAteams[3].tPD, NAteams[4].tPD]
        })
        self.SA = pd.DataFrame({
            'Team': [SAteams[0], SAteams[1], SAteams[2], SAteams[3], SAteams[4]],
            'ABR ': [SAteams[0].ABR, SAteams[1].ABR, SAteams[2].ABR, SAteams[3].ABR, SAteams[4].ABR],
            'Played': [SAteams[0].played, SAteams[1].played, SAteams[2].played, SAteams[3].played, SAteams[4].played],
            'Stage Wins': [SAteams[0].wins, SAteams[1].wins, SAteams[2].wins, SAteams[3].wins, SAteams[4].wins],
            'Stage PD': [SAteams[0].pD, SAteams[1].pD, SAteams[2].pD, SAteams[3].pD, SAteams[4].pD],
            'Season Wins': [SAteams[0].tWins, SAteams[1].tWins, SAteams[2].tWins, SAteams[3].tWins, SAteams[4].tWins],
            'Season PD': [SAteams[0].tPD, SAteams[1].tPD, SAteams[2].tPD, SAteams[3].tPD, SAteams[4].tPD]

        })
        self.WE = pd.DataFrame({
            'Team': [WEteams[0], WEteams[1], WEteams[2], WEteams[3], WEteams[4]],
            'ABR ': [WEteams[0].ABR, WEteams[1].ABR, WEteams[2].ABR, WEteams[3].ABR, WEteams[4].ABR],
            'Played': [WEteams[0].played, WEteams[1].played, WEteams[2].played, WEteams[3].played, WEteams[4].played],
            'Stage Wins': [WEteams[0].wins, WEteams[1].wins, WEteams[2].wins, WEteams[3].wins, WEteams[4].wins],
            'Stage PD': [WEteams[0].pD, WEteams[1].pD, WEteams[2].pD, WEteams[3].pD, WEteams[4].pD],
            'Season Wins': [WEteams[0].tWins, WEteams[1].tWins, WEteams[2].tWins, WEteams[3].tWins, WEteams[4].tWins],
            'Season PD': [WEteams[0].tPD, WEteams[1].tPD, WEteams[2].tPD, WEteams[3].tPD, WEteams[4].tPD]
        })
        self.EE = pd.DataFrame({
            'Team': [EEteams[0], EEteams[1], EEteams[2], EEteams[3], EEteams[4]],
            'ABR ': [EEteams[0].ABR, EEteams[1].ABR, EEteams[2].ABR, EEteams[3].ABR, EEteams[4].ABR],
            'Played': [EEteams[0].played, EEteams[1].played, EEteams[2].played, EEteams[3].played, EEteams[4].played],
            'Stage Wins': [EEteams[0].wins, EEteams[1].wins, EEteams[2].wins, EEteams[3].wins, EEteams[4].wins],
            'Stage PD': [EEteams[0].pD, EEteams[1].pD, EEteams[2].pD, EEteams[3].pD, EEteams[4].pD],
            'Season Wins': [EEteams[0].tWins, EEteams[1].tWins, EEteams[2].tWins, EEteams[3].tWins, EEteams[4].tWins],
            'Season PD': [EEteams[0].tPD, EEteams[1].tPD, EEteams[2].tPD, EEteams[3].tPD, EEteams[4].tPD]
        })
        self.AF = pd.DataFrame({
            'Team': [AFteams[0], AFteams[1], AFteams[2], AFteams[3], AFteams[4]],
            'ABR ': [AFteams[0].ABR, AFteams[1].ABR, AFteams[2].ABR, AFteams[3].ABR, AFteams[4].ABR],
            'Played': [AFteams[0].played, AFteams[1].played, AFteams[2].played, AFteams[3].played, AFteams[4].played],
            'Stage Wins': [AFteams[0].wins, AFteams[1].wins, AFteams[2].wins, AFteams[3].wins, AFteams[4].wins],
            'Stage PD': [AFteams[0].pD, AFteams[1].pD, AFteams[2].pD, AFteams[3].pD, AFteams[4].pD],
            'Season Wins': [AFteams[0].tWins, AFteams[1].tWins, AFteams[2].tWins, AFteams[3].tWins, AFteams[4].tWins],
            'Season PD': [AFteams[0].tPD, AFteams[1].tPD, AFteams[2].tPD, AFteams[3].tPD, AFteams[4].tPD]
        })
        self.OC = pd.DataFrame({
            'Team': [OCteams[0], OCteams[1], OCteams[2], OCteams[3], OCteams[4]],
            'ABR ': [OCteams[0].ABR, OCteams[1].ABR, OCteams[2].ABR, OCteams[3].ABR, OCteams[4].ABR],
            'Played': [OCteams[0].played, OCteams[1].played, OCteams[2].played, OCteams[3].played, OCteams[4].played],
            'Stage Wins': [OCteams[0].wins, OCteams[1].wins, OCteams[2].wins, OCteams[3].wins, OCteams[4].wins],
            'Stage PD': [OCteams[0].pD, OCteams[1].pD, OCteams[2].pD, OCteams[3].pD, OCteams[4].pD],
            'Season Wins': [OCteams[0].tWins, OCteams[1].tWins, OCteams[2].tWins, OCteams[3].tWins, OCteams[4].tWins],
            'Season PD': [OCteams[0].tPD, OCteams[1].tPD, OCteams[2].tPD, OCteams[3].tPD, OCteams[4].tPD]
        })
        self.WA = pd.DataFrame({
            'Team': [WAteams[0], WAteams[1], WAteams[2], WAteams[3], WAteams[4]],
            'ABR ': [WAteams[0].ABR, WAteams[1].ABR, WAteams[2].ABR, WAteams[3].ABR, WAteams[4].ABR],
            'Played': [WAteams[0].played, WAteams[1].played, WAteams[2].played, WAteams[3].played, WAteams[4].played],
            'Stage Wins': [WAteams[0].wins, WAteams[1].wins, WAteams[2].wins, WAteams[3].wins, WAteams[4].wins],
            'Stage PD': [WAteams[0].pD, WAteams[1].pD, WAteams[2].pD, WAteams[3].pD, WAteams[4].pD],
            'Season Wins': [WAteams[0].tWins, WAteams[1].tWins, WAteams[2].tWins, WAteams[3].tWins, WAteams[4].tWins],
            'Season PD': [WAteams[0].tPD, WAteams[1].tPD, WAteams[2].tPD, WAteams[3].tPD, WAteams[4].tPD]
        })
        self.EA = pd.DataFrame({
            'Team': [EAteams[0], EAteams[1], EAteams[2], EAteams[3], EAteams[4]],
            'ABR ': [EAteams[0].ABR, EAteams[1].ABR, EAteams[2].ABR, EAteams[3].ABR, EAteams[4].ABR],
            'Played': [EAteams[0].played, EAteams[1].played, EAteams[2].played, EAteams[3].played, EAteams[4].played],
            'Stage Wins': [EAteams[0].wins, EAteams[1].wins, EAteams[2].wins, EAteams[3].wins, EAteams[4].wins],
            'Stage PD': [EAteams[0].pD, EAteams[1].pD, EAteams[2].pD, EAteams[3].pD, EAteams[4].pD],
            'Season Wins': [EAteams[0].tWins, EAteams[1].tWins, EAteams[2].tWins, EAteams[3].tWins, EAteams[4].tWins],
            'Season PD': [EAteams[0].tPD, EAteams[1].tPD, EAteams[2].tPD, EAteams[3].tPD, EAteams[4].tPD]
        })
        self.Divisions = [self.NA, self.SA, self.WE, self.EE, self.AF, self.OC, self.WA, self.EA]

    def stage(self):
        for q in range(1):  # This is a slightly edited of a round robin algorithm i found online and stole
            schedule = []
            for div in self.Divisions:
                w = list(div['Team'].copy())
                random.shuffle(w)
                if len(w) % 2 == 1:
                    w.append(None)
                n = len(w)
                d = list(range(n))
                mid = n // 2
                for i in range(n - 1):
                    l1 = d[:mid]
                    l2 = d[mid:]
                    l2.reverse()
                    round = []
                    for j in range(mid):
                        t1 = w[l1[j]]
                        t2 = w[l2[j]]
                        if j == 0 and i % 2 == 1:
                            round.append((t2, t1))
                        else:
                            round.append((t1, t2))
                    schedule.append(round)
                    # rotate list by n/2, leaving last element at the end
                    d = d[mid:-1] + d[:mid] + d[-1:]
            for y in range(5):
                print('Round ' + str(y + 1))
                #y = y % 29
                for bloop in range(8):
                    for z in schedule[y + (5 * bloop)]:
                        if z[0] is not None and z[1] is not None:
                            game(z[0], z[1], ends=6)
            for y in range(5):
                print('Round ' + str(y + 6))
                for bloop in range(8):
                    for z in schedule[y + (5*bloop)]:
                        if z[0] is not None and z[1] is not None:
                            game(z[1], z[0], ends=6)

    def stageplayoffs(self, teams):
        random.shuffle(teams)
        self.bracket(teams)
        print('Hosted by:', self.citySelect(teams))
        Q1 = game(teams[0], teams[1], p=1, playoff=True, neutral=True)
        Q2 = game(teams[2], teams[3], p=1, playoff=True, neutral=True)
        Q3 = game(teams[4], teams[5], p=1, playoff=True, neutral=True)
        Q4 = game(teams[6], teams[7], p=1, playoff=True, neutral=True)
        S1 = game(Q1, Q2, p=1, playoff=True, neutral=True)
        S2 = game(Q3, Q4, p=1, playoff=True, neutral=True)
        F = game(S1, S2, p=1, playoff=True, neutral=True)
        print(F, 'wins the stage playoffs!')

    def standings(self, part='Stage'):
        self.tableRefresh()
        for i in self.Divisions:
            i.sort_values(by=[part+' Wins', part+' PD'], ascending=False, inplace=True)
            print(i)

    def stageReset(self):
        for i in self.Divisions:
            for j in i['Team']:
                j.wins = 0
                j.pD = 0

    def bracket(self, teams):
        print()
        print(teams[0].ABR+'|')
        print('   |___')
        print(teams[1].ABR+'|    |')
        print('        |___')
        print(teams[2].ABR+'|    |   |')
        print('   |____|   |')
        print(teams[3].ABR+'|        |')
        print('            |___')
        print(teams[4].ABR+'|        |')
        print('   |____    |')
        print(teams[5].ABR+'|    |   |')
        print('        |___|')
        print(teams[6].ABR+'|    |')
        print('   |____|')
        print(teams[7].ABR+'|')

    def playins(self):
        print('Play-ins!')
        winners = []
        for i in self.Divisions:
            winners.append(game(i['Team'].iloc[1], i['Team'].iloc[2], p=1, playoff=True))
        return winners

    def playoffs(self, tops, bottoms):
        nums = [0, 1, 2, 3, 4, 5, 6, 7]
        random.shuffle(nums)
        print('Round 1, best of 3')
        R1 = self.series(tops[nums[0]], bottoms[nums[1]], 2)
        R2 = self.series(tops[nums[2]], bottoms[nums[3]], 2)
        R3 = self.series(tops[nums[4]], bottoms[nums[5]], 2)
        R4 = self.series(tops[nums[6]], bottoms[nums[7]], 2)
        R5 = self.series(tops[nums[1]], bottoms[nums[0]], 2)
        R6 = self.series(tops[nums[3]], bottoms[nums[2]], 2)
        R7 = self.series(tops[nums[5]], bottoms[nums[4]], 2)
        R8 = self.series(tops[nums[7]], bottoms[nums[6]], 2)
        print('Quarterfinals, best of 5')
        self.bracket([R1, R2, R3, R4, R5, R6, R7, R8])
        if R1.tWins > R2.tWins:
            Q1 = self.series(R1, R2, 3)
        elif R2.tWins > R1.tWins:
            Q1 = self.series(R2, R1, 3)
        else:
            Q1 = self.series(R1, R2, 3, neu=True)
        if R3.tWins > R4.tWins:
            Q2 = self.series(R3, R4, 3)
        elif R4.tWins > R3.tWins:
            Q2 = self.series(R4, R3, 3)
        else:
            Q2 = self.series(R3, R4, 3, neu=True)
        if R5.tWins > R6.tWins:
            Q3 = self.series(R5, R6, 3)
        elif R6.tWins > R5.tWins:
            Q3 = self.series(R6, R5, 3)
        else:
            Q3 = self.series(R5, R6, 3, neu=True)
        if R7.tWins > R8.tWins:
            Q4 = self.series(R7, R8, 3)
        elif R8.tWins > R7.tWins:
            Q4 = self.series(R8, R7, 3)
        else:
            Q4 = self.series(R7, R8, 3, neu=True)
        print('Semifinals, best of 7')
        print('FINAL FOUR HOSTED BY', self.citySelect([Q1, Q2, Q3, Q4]))
        S1 = self.series(Q1, Q2, 4, neu=True, host=False)
        S2 = self.series(Q3, Q4, 4, neu=True, host=False)
        print('Grand Finals!!!, best of 7')
        F = self.series(S1, S2, 4, neu=True, host=False)
        print(F, 'wins the WORLD TITLE')

    def series(self, x, y, n, neu=False, host=True):
        if not neu and host:
            host = x
        else:
            host = self.citySelect([x, y])
        print(x, 'vs.', y, 'hosted by', host)
        xWins = 0
        yWins = 0
        while xWins < n and yWins < n:
            single = game(x, y, p=1, playoff=True, neutral=neu)
            if single == x:
                xWins += 1
            else:
                yWins += 1
            print('Series Score:', x.ABR, xWins, yWins, y.ABR)
        if xWins == n:
            return x
        else:
            return y

    def citySelect(self, blacklist):
        city = random.choice(self.Cities)
        while city in blacklist:
            city = random.choice(self.Cities)
        return city

def playIt():
    NCL = League()
    NCL.stage()
    NCL.standings()
    NCL.stageplayoffs([NCL.NA['Team'].iloc[0], NCL.SA['Team'].iloc[0], NCL.WE['Team'].iloc[0], NCL.EE['Team'].iloc[0], NCL.AF['Team'].iloc[0], NCL.OC['Team'].iloc[0], NCL.WA['Team'].iloc[0], NCL.EA['Team'].iloc[0]])
    NCL.stageReset()
    NCL.stage()
    NCL.standings()
    NCL.stageplayoffs([NCL.NA['Team'].iloc[0], NCL.SA['Team'].iloc[0], NCL.WE['Team'].iloc[0], NCL.EE['Team'].iloc[0], NCL.AF['Team'].iloc[0], NCL.OC['Team'].iloc[0], NCL.WA['Team'].iloc[0], NCL.EA['Team'].iloc[0]])
    NCL.stageReset()
    NCL.stage()
    NCL.standings()
    NCL.stageplayoffs([NCL.NA['Team'].iloc[0], NCL.SA['Team'].iloc[0], NCL.WE['Team'].iloc[0], NCL.EE['Team'].iloc[0], NCL.AF['Team'].iloc[0], NCL.OC['Team'].iloc[0], NCL.WA['Team'].iloc[0], NCL.EA['Team'].iloc[0]])
    NCL.stageReset()
    NCL.standings('Season')
    seed2 = NCL.playins()
    NCL.playoffs([NCL.NA['Team'].iloc[0], NCL.SA['Team'].iloc[0], NCL.WE['Team'].iloc[0], NCL.EE['Team'].iloc[0], NCL.AF['Team'].iloc[0], NCL.OC['Team'].iloc[0], NCL.WA['Team'].iloc[0], NCL.EA['Team'].iloc[0]], seed2)

