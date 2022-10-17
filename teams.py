"""
    Pull in team data via API
"""
import pandas as pd
import cfbd

class Team:
    def __init__(self, name, talent, abbreviation, conference,
                 division, color, mascot, city, state
                 ):
         self.name = name
         self.talent = talent
         self.abbreviation = abbreviation
         self.conference = conference
         self.division = division
         self.color = color
         self.mascot = mascot
         self.city = city
         self.state = state
         self.roster = []
    
    def add(self, player):
        self.roster.append(player)
    
    def __str__(self):
        return f"{self.name} ({self.abbreviation}) Conference: {self.conference} (Rating: {self.talent})"
    
    def printRoster(self):
        for p in self.roster:
            print(str(p))
    
class Player:
    def __init__(self, team, position, first, last, year,
                 height, weight, jersey):
        self.team = team
        self.position = position
        self.first = first
        self.last = last
        self.year = year
        self.height = height
        self.weight = weight
        self.jersey = jersey
    
    def __str__(self):
        return f"{self.first} {self.last}"

configuration = cfbd.Configuration()
configuration.api_key['Authorization'] = 'l+/5SBSLGDZrqfl1tXTNDgRykUC0zop9LuzfxABb5uaCNW3BQPNcwrcZud+CNALp'
configuration.api_key_prefix['Authorization'] = 'Bearer'

api_instance = cfbd.TeamsApi(cfbd.ApiClient(configuration))
teams = api_instance.get_fbs_teams()
teams_df = pd.DataFrame.from_records([dict(team=t.school, abbreviation=t.abbreviation, conference=t.conference, division=t.division, color=t.color, 
                                           mascot = t.mascot, city=t.location.city, state=t.location.state) for t in teams])

talents = api_instance.get_talent(year=2022)
talents_df = pd.DataFrame.from_records([dict(team=t.school, rating=t.talent) for t in talents])

teams_df = pd.merge(talents_df, teams_df, on="team", how="inner")

rosters = api_instance.get_roster()
rosters_df = pd.DataFrame.from_records([dict(team = r.team, position=r.position, firstName =r.first_name, lastName = r.last_name, 
                                             year=r.year, height = r.height, weight = r.weight, jersey = r.jersey) for r in rosters])

def getTeamsAndRosters():
    teams = []
    for i in teams_df.index:
        teams.append(Team((teams_df['team'][i]), (teams_df['rating'][i]), (teams_df['abbreviation'][i]), (teams_df['conference'][i]), 
                        (teams_df['division'][i]), (teams_df['color'][i]), (teams_df['mascot'][i]), 
                        (teams_df['city'][i]), (teams_df['state'][i])))
    players = []
    for i in rosters_df.index:
        players.append(Player((rosters_df['team'][i]), (rosters_df['position'][i]), (rosters_df['firstName'][i]), 
                        (rosters_df['lastName'][i]), (rosters_df['year'][i]), (rosters_df['height'][i]), 
                        (rosters_df['weight'][i]), (rosters_df['jersey'][i])))

    for t in teams:
        for p in players:
            if p.team == t.name:
                t.add(p)
    
    return teams

def selectTeam(teams):
    i = 1
    for team in teams:
        print("[" + str(i) + "] " + str(team))
        i += 1

    

