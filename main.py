"""
    Author: ebrown
    Date: 2022/10/16
    Purpose: Basic college football simulation game
"""

import time
from numpy import integer
import teams

print("Loading...")
time.sleep(10)
allTeams = teams.getTeamsAndRosters()
print("Welcome to this early command line version of a college football simulator!")
print("Rosters are automatically updated, with support coming for historical rosters in future builds.")
print("First, select the home team:")
teams.selectTeam(allTeams)
homeTeam = int(input("Home Team: "))
if (homeTeam < 1 or homeTeam > 130):
    print("Please use the corresponding # on the left to select a team.")
    homeTeam = input("Home Team: ")
else:
    home = allTeams[homeTeam-1]
    teams.selectTeam(allTeams)
    print(str(home) + " vs")
awayTeam = int(input("Away Team: "))
if (awayTeam == homeTeam) or (awayTeam < 1 or awayTeam > 130):
    print("Please use the corresponding # on the left to select a team.")
    awayTeam = input("Away Team: ")
else:
    away = allTeams[awayTeam-1]
    print(str(home) + " vs " + str(away))
    
    
    