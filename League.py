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
            'Wins': [NAteams[0].wins, NAteams[1].wins, NAteams[2].wins, NAteams[3].wins, NAteams[4].wins],
            'PD': [NAteams[0].pD, NAteams[1].pD, NAteams[2].pD, NAteams[3].pD, NAteams[4].pD]
        })
        self.SA = pd.DataFrame({
            'Team': [SAteams[0], SAteams[1], SAteams[2], SAteams[3], SAteams[4]],
            'ABR ': [SAteams[0].ABR, SAteams[1].ABR, SAteams[2].ABR, SAteams[3].ABR, SAteams[4].ABR],
            'Played': [SAteams[0].played, SAteams[1].played, SAteams[2].played, SAteams[3].played, SAteams[4].played],
            'Wins': [SAteams[0].wins, SAteams[1].wins, SAteams[2].wins, SAteams[3].wins, SAteams[4].wins],
            'PD': [SAteams[0].pD, SAteams[1].pD, SAteams[2].pD, SAteams[3].pD, SAteams[4].pD]

        })
        self.WE = pd.DataFrame({
            'Team': [WEteams[0], WEteams[1], WEteams[2], WEteams[3], WEteams[4]],
            'ABR ': [WEteams[0].ABR, WEteams[1].ABR, WEteams[2].ABR, WEteams[3].ABR, WEteams[4].ABR],
            'Played': [WEteams[0].played, WEteams[1].played, WEteams[2].played, WEteams[3].played, WEteams[4].played],
            'Wins': [WEteams[0].wins, WEteams[1].wins, WEteams[2].wins, WEteams[3].wins, WEteams[4].wins],
            'PD': [WEteams[0].pD, WEteams[1].pD, WEteams[2].pD, WEteams[3].pD, WEteams[4].pD]

        })
        self.EE = pd.DataFrame({
            'Team': [EEteams[0], EEteams[1], EEteams[2], EEteams[3], EEteams[4]],
            'ABR ': [EEteams[0].ABR, EEteams[1].ABR, EEteams[2].ABR, EEteams[3].ABR, EEteams[4].ABR],
            'Played': [EEteams[0].played, EEteams[1].played, EEteams[2].played, EEteams[3].played, EEteams[4].played],
            'Wins': [EEteams[0].wins, EEteams[1].wins, EEteams[2].wins, EEteams[3].wins, EEteams[4].wins],
            'PD': [EEteams[0].pD, EEteams[1].pD, EEteams[2].pD, EEteams[3].pD, EEteams[4].pD]
        })
        self.AF = pd.DataFrame({
            'Team': [AFteams[0], AFteams[1], AFteams[2], AFteams[3], AFteams[4]],
            'ABR ': [AFteams[0].ABR, AFteams[1].ABR, AFteams[2].ABR, AFteams[3].ABR, AFteams[4].ABR],
            'Played': [AFteams[0].played, AFteams[1].played, AFteams[2].played, AFteams[3].played, AFteams[4].played],
            'Wins': [AFteams[0].wins, AFteams[1].wins, AFteams[2].wins, AFteams[3].wins, AFteams[4].wins],
            'PD': [AFteams[0].pD, AFteams[1].pD, AFteams[2].pD, AFteams[3].pD, AFteams[4].pD]
        })
        self.OC = pd.DataFrame({
            'Team': [OCteams[0], OCteams[1], OCteams[2], OCteams[3], OCteams[4]],
            'ABR ': [OCteams[0].ABR, OCteams[1].ABR, OCteams[2].ABR, OCteams[3].ABR, OCteams[4].ABR],
            'Played': [OCteams[0].played, OCteams[1].played, OCteams[2].played, OCteams[3].played, OCteams[4].played],
            'Wins': [OCteams[0].wins, OCteams[1].wins, OCteams[2].wins, OCteams[3].wins, OCteams[4].wins],
            'PD': [OCteams[0].pD, OCteams[1].pD, OCteams[2].pD, OCteams[3].pD, OCteams[4].pD]
        })
        self.WA = pd.DataFrame({
            'Team': [WAteams[0], WAteams[1], WAteams[2], WAteams[3], WAteams[4]],
            'ABR ': [WAteams[0].ABR, WAteams[1].ABR, WAteams[2].ABR, WAteams[3].ABR, WAteams[4].ABR],
            'Played': [WAteams[0].played, WAteams[1].played, WAteams[2].played, WAteams[3].played, WAteams[4].played],
            'Wins': [WAteams[0].wins, WAteams[1].wins, WAteams[2].wins, WAteams[3].wins, WAteams[4].wins],
            'PD': [WAteams[0].pD, WAteams[1].pD, WAteams[2].pD, WAteams[3].pD, WAteams[4].pD]
        })
        self.EA = pd.DataFrame({
            'Team': [EAteams[0], EAteams[1], EAteams[2], EAteams[3], EAteams[4]],
            'ABR ': [EAteams[0].ABR, EAteams[1].ABR, EAteams[2].ABR, EAteams[3].ABR, EAteams[4].ABR],
            'Played': [EAteams[0].played, EAteams[1].played, EAteams[2].played, EAteams[3].played, EAteams[4].played],
            'Wins': [EAteams[0].wins, EAteams[1].wins, EAteams[2].wins, EAteams[3].wins, EAteams[4].wins],
            'PD': [EAteams[0].pD, EAteams[1].pD, EAteams[2].pD, EAteams[3].pD, EAteams[4].pD]
        })
        self.Divisions = [self.NA, self.SA, self.WE, self.EE, self.AF, self.OC, self.WA, self.EA]

    def tableRefresh(self):
        self.NA = pd.DataFrame({
                'Team': [NAteams[0], NAteams[1], NAteams[2], NAteams[3], NAteams[4]],
                'ABR ': [NAteams[0].ABR, NAteams[1].ABR, NAteams[2].ABR, NAteams[3].ABR, NAteams[4].ABR],
                'Played': [NAteams[0].played, NAteams[1].played, NAteams[2].played, NAteams[3].played, NAteams[4].played],
                'Wins': [NAteams[0].wins, NAteams[1].wins, NAteams[2].wins, NAteams[3].wins, NAteams[4].wins],
                'PD': [NAteams[0].pD, NAteams[1].pD, NAteams[2].pD, NAteams[3].pD, NAteams[4].pD]
            })
        self.SA = pd.DataFrame({
                'Team': [SAteams[0], SAteams[1], SAteams[2], SAteams[3], SAteams[4]],
                'ABR ': [SAteams[0].ABR, SAteams[1].ABR, SAteams[2].ABR, SAteams[3].ABR, SAteams[4].ABR],
                'Played': [SAteams[0].played, SAteams[1].played, SAteams[2].played, SAteams[3].played, SAteams[4].played],
                'Wins': [SAteams[0].wins, SAteams[1].wins, SAteams[2].wins, SAteams[3].wins, SAteams[4].wins],
                'PD': [SAteams[0].pD, SAteams[1].pD, SAteams[2].pD, SAteams[3].pD, SAteams[4].pD]

            })
        self.WE = pd.DataFrame({
                'Team': [WEteams[0], WEteams[1], WEteams[2], WEteams[3], WEteams[4]],
                'ABR ': [WEteams[0].ABR, WEteams[1].ABR, WEteams[2].ABR, WEteams[3].ABR, WEteams[4].ABR],
                'Played': [WEteams[0].played, WEteams[1].played, WEteams[2].played, WEteams[3].played, WEteams[4].played],
                'Wins': [WEteams[0].wins, WEteams[1].wins, WEteams[2].wins, WEteams[3].wins, WEteams[4].wins],
                'PD': [WEteams[0].pD, WEteams[1].pD, WEteams[2].pD, WEteams[3].pD, WEteams[4].pD]

            })
        self.EE = pd.DataFrame({
                'Team': [EEteams[0], EEteams[1], EEteams[2], EEteams[3], EEteams[4]],
                'ABR ': [EEteams[0].ABR, EEteams[1].ABR, EEteams[2].ABR, EEteams[3].ABR, EEteams[4].ABR],
                'Played': [EEteams[0].played, EEteams[1].played, EEteams[2].played, EEteams[3].played, EEteams[4].played],
                'Wins': [EEteams[0].wins, EEteams[1].wins, EEteams[2].wins, EEteams[3].wins, EEteams[4].wins],
                'PD': [EEteams[0].pD, EEteams[1].pD, EEteams[2].pD, EEteams[3].pD, EEteams[4].pD]
            })
        self.AF = pd.DataFrame({
                'Team': [AFteams[0], AFteams[1], AFteams[2], AFteams[3], AFteams[4]],
                'ABR ': [AFteams[0].ABR, AFteams[1].ABR, AFteams[2].ABR, AFteams[3].ABR, AFteams[4].ABR],
                'Played': [AFteams[0].played, AFteams[1].played, AFteams[2].played, AFteams[3].played, AFteams[4].played],
                'Wins': [AFteams[0].wins, AFteams[1].wins, AFteams[2].wins, AFteams[3].wins, AFteams[4].wins],
                'PD': [AFteams[0].pD, AFteams[1].pD, AFteams[2].pD, AFteams[3].pD, AFteams[4].pD]
            })
        self.OC = pd.DataFrame({
                'Team': [OCteams[0], OCteams[1], OCteams[2], OCteams[3], OCteams[4]],
                'ABR ': [OCteams[0].ABR, OCteams[1].ABR, OCteams[2].ABR, OCteams[3].ABR, OCteams[4].ABR],
                'Played': [OCteams[0].played, OCteams[1].played, OCteams[2].played, OCteams[3].played, OCteams[4].played],
                'Wins': [OCteams[0].wins, OCteams[1].wins, OCteams[2].wins, OCteams[3].wins, OCteams[4].wins],
                'PD': [OCteams[0].pD, OCteams[1].pD, OCteams[2].pD, OCteams[3].pD, OCteams[4].pD]
            })
        self.WA = pd.DataFrame({
                'Team': [WAteams[0], WAteams[1], WAteams[2], WAteams[3], WAteams[4]],
                'ABR ': [WAteams[0].ABR, WAteams[1].ABR, WAteams[2].ABR, WAteams[3].ABR, WAteams[4].ABR],
                'Played': [WAteams[0].played, WAteams[1].played, WAteams[2].played, WAteams[3].played, WAteams[4].played],
                'Wins': [WAteams[0].wins, WAteams[1].wins, WAteams[2].wins, WAteams[3].wins, WAteams[4].wins],
                'PD': [WAteams[0].pD, WAteams[1].pD, WAteams[2].pD, WAteams[3].pD, WAteams[4].pD]
            })
        self.EA = pd.DataFrame({
                'Team': [EAteams[0], EAteams[1], EAteams[2], EAteams[3], EAteams[4]],
                'ABR ': [EAteams[0].ABR, EAteams[1].ABR, EAteams[2].ABR, EAteams[3].ABR, EAteams[4].ABR],
                'Played': [EAteams[0].played, EAteams[1].played, EAteams[2].played, EAteams[3].played, EAteams[4].played],
                'Wins': [EAteams[0].wins, EAteams[1].wins, EAteams[2].wins, EAteams[3].wins, EAteams[4].wins],
                'PD': [EAteams[0].pD, EAteams[1].pD, EAteams[2].pD, EAteams[3].pD, EAteams[4].pD]
            })
        self.Divisions = [self.NA, self.SA, self.WE, self.EE, self.AF, self.OC, self.WA, self.EA]

    def stage1(self):
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
                for z in schedule[y]:
                    if z[0] is not None and z[1] is not None:
                        game(z[0], z[1], ends=6)
                for z in schedule[y + 5]:
                    if z[0] is not None and z[1] is not None:
                        game(z[0], z[1], ends=6)
                for z in schedule[y + 10]:
                    if z[0] is not None and z[1] is not None:
                        game(z[0], z[1], ends=6)
                for z in schedule[y + 15]:
                    if z[0] is not None and z[1] is not None:
                        game(z[0], z[1], ends=6)
                for z in schedule[y + 20]:
                    if z[0] is not None and z[1] is not None:
                        game(z[0], z[1], ends=6)
                for z in schedule[y + 25]:
                    if z[0] is not None and z[1] is not None:
                        game(z[0], z[1], ends=6)
                for z in schedule[y + 30]:
                    if z[0] is not None and z[1] is not None:
                        game(z[0], z[1], ends=6)
                for z in schedule[y + 35]:
                    if z[0] is not None and z[1] is not None:
                        game(z[0], z[1], ends=6)
            for y in range(5):
                print('Round ' + str(y + 6))
                for z in schedule[y]:
                    if z[0] is not None and z[1] is not None:
                        game(z[1], z[0], ends=6)
                for z in schedule[y + 5]:
                    if z[0] is not None and z[1] is not None:
                        game(z[1], z[0], ends=6)
                for z in schedule[y + 10]:
                    if z[0] is not None and z[1] is not None:
                        game(z[1], z[0], ends=6)
                for z in schedule[y + 15]:
                    if z[0] is not None and z[1] is not None:
                        game(z[1], z[0], ends=6)
                for z in schedule[y + 20]:
                    if z[0] is not None and z[1] is not None:
                        game(z[1], z[0], ends=6)
                for z in schedule[y + 25]:
                    if z[0] is not None and z[1] is not None:
                        game(z[1], z[0], ends=6)
                for z in schedule[y + 30]:
                    if z[0] is not None and z[1] is not None:
                        game(z[1], z[0], ends=6)
                for z in schedule[y + 35]:
                    if z[0] is not None and z[1] is not None:
                        game(z[1], z[0], ends=6)

    def stage1playoffs(self, teams):
        random.shuffle(teams)
        self.bracket(teams)
        Q1 = game(teams[0], teams[1], p=1, playoff=True, neutral=True)
        Q2 = game(teams[2], teams[3], p=1, playoff=True, neutral=True)
        Q3 = game(teams[4], teams[5], p=1, playoff=True, neutral=True)
        Q4 = game(teams[6], teams[7], p=1, playoff=True, neutral=True)
        S1 = game(Q1, Q2, p=1, playoff=True, neutral=True)
        S2 = game(Q3, Q4, p=1, playoff=True, neutral=True)
        F = game(S1, S2, p=1, playoff=True, neutral=True)
        print(F, 'wins the stage 1 playoffs!')

    def standings(self):
        self.tableRefresh()
        for i in self.Divisions:
            i.sort_values(by=['Wins', 'PD'], ascending=False, inplace=True)
            print(i)

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


NCL = League()
NCL.stage1()
NCL.standings()
NCL.stage1playoffs([NCL.NA['Team'].iloc[0], NCL.SA['Team'].iloc[0], NCL.WE['Team'].iloc[0], NCL.EE['Team'].iloc[0], NCL.AF['Team'].iloc[0], NCL.OC['Team'].iloc[0], NCL.WA['Team'].iloc[0], NCL.EA['Team'].iloc[0]])
