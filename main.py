import requests
import json
#import self
import matplotlib.pyplot as plt
print("Welcome to BucketAnalytics! Analyze your favorite NBA teams' daily performances and see how they compare against other teams in the league! Click Enter to get Started!")
enter = input()
'''
response = requests.get(
    "https://cdn.nba.com/static/json/liveData/scoreboard/todaysScoreboard_00.json"
)
obj = json.loads(response.text)
''' 
data_set = {
  "meta": {
    "version": 1,
    "request": "https://nba-prod-us-east-1-mediaops-stats.s3.amazonaws.com/NBA/liveData/scoreboard/todaysScoreboard_00.json",
    "time": "2021-02-21 01:49:06.496",
    "code": 200
  },
  "scoreboard": {
    "gameDate": "2021-02-20",
    "leagueId": "00",
    "leagueName": "National Basketball Association",
    "games": [
      {
        "gameId": "0022000458",
        "gameCode": "20210220/SASNYK",
        "gameStatus": 1,
        "gameStatusText": "PPD",
        "period": 0,
        "gameClock": "",
        "gameTimeUTC": "2021-02-20T18:00:00Z",
        "gameEt": "2021-02-20T13:00:00Z",
        "regulationPeriods": 4,
        "seriesGameNumber": "",
        "seriesText": "",
        "homeTeam": {
          "teamId": 1610612752,
          "teamName": "Knicks",
          "teamCity": "New York",
          "teamTricode": "NYK",
          "wins": 14,
          "losses": 16,
          "score": 0,
          "timeoutsRemaining": 0,
          "periods": [
            {
              "period": 1,
              "periodType": "REGULAR",
              "score": 0
            },
            {
              "period": 2,
              "periodType": "REGULAR",
              "score": 0
            },
            {
              "period": 3,
              "periodType": "REGULAR",
              "score": 0
            },
            {
              "period": 4,
              "periodType": "REGULAR",
              "score": 0
            }
          ]
        },
        "awayTeam": {
          "teamId": 1610612759,
          "teamName": "Spurs",
          "teamCity": "San Antonio",
          "teamTricode": "SAS",
          "wins": 16,
          "losses": 11,
          "score": 0,
          "timeoutsRemaining": 0,
          "periods": [
            {
              "period": 1,
              "periodType": "REGULAR",
              "score": 0
            },
            {
              "period": 2,
              "periodType": "REGULAR",
              "score": 0
            },
            {
              "period": 3,
              "periodType": "REGULAR",
              "score": 0
            },
            {
              "period": 4,
              "periodType": "REGULAR",
              "score": 0
            }
          ]
        },
        "gameLeaders": {
          "homeLeaders": {
            "personId": 0,
            "name": "",
            "jerseyNum": "",
            "position": "",
            "teamTricode": "NYK",
            "points": 0,
            "rebounds": 0,
            "assists": 0
          },
          "awayLeaders": {
            "personId": 0,
            "name": "",
            "jerseyNum": "",
            "position": "",
            "teamTricode": "SAS",
            "points": 0,
            "rebounds": 0,
            "assists": 0
          }
        },
        "pbOdds": {
          "odds": 0.0,
          "suspended": 1
        }
      },
      {
        "gameId": "0022000459",
        "gameCode": "20210220/GSWCHA",
        "gameStatus": 3,
        "gameStatusText": "Final",
        "period": 4,
        "gameClock": "",
        "gameTimeUTC": "2021-02-21T01:00:00Z",
        "gameEt": "2021-02-20T20:00:00Z",
        "regulationPeriods": 4,
        "seriesGameNumber": "",
        "seriesText": "",
        "homeTeam": {
          "teamId": 1610612766,
          "teamName": "Hornets",
          "teamCity": "Charlotte",
          "teamTricode": "CHA",
          "wins": 14,
          "losses": 15,
          "score": 102,
          "timeoutsRemaining": 0,
          "periods": [
            {
              "period": 1,
              "periodType": "REGULAR",
              "score": 24
            },
            {
              "period": 2,
              "periodType": "REGULAR",
              "score": 21
            },
            {
              "period": 3,
              "periodType": "REGULAR",
              "score": 24
            },
            {
              "period": 4,
              "periodType": "REGULAR",
              "score": 33
            }
          ]
        },
        "awayTeam": {
          "teamId": 1610612744,
          "teamName": "Warriors",
          "teamCity": "Golden State",
          "teamTricode": "GSW",
          "wins": 16,
          "losses": 15,
          "score": 100,
          "timeoutsRemaining": 1,
          "periods": [
            {
              "period": 1,
              "periodType": "REGULAR",
              "score": 15
            },
            {
              "period": 2,
              "periodType": "REGULAR",
              "score": 32
            },
            {
              "period": 3,
              "periodType": "REGULAR",
              "score": 22
            },
            {
              "period": 4,
              "periodType": "REGULAR",
              "score": 31
            }
          ]
        },
        "gameLeaders": {
          "homeLeaders": {
            "personId": 1626179,
            "name": "Terry Rozier",
            "jerseyNum": "3",
            "position": "G",
            "teamTricode": "CHA",
            "points": 36,
            "rebounds": 3,
            "assists": 4
          },
          "awayLeaders": {
            "personId": 1626162,
            "name": "Kelly Oubre Jr.",
            "jerseyNum": "12",
            "position": "F-G",
            "teamTricode": "GSW",
            "points": 25,
            "rebounds": 6,
            "assists": 1
          }
        },
        "pbOdds": {
          "odds": 0.0,
          "suspended": 1
        }
      },
      {
        "gameId": "0022000461",
        "gameCode": "20210220/INDHOU",
        "gameStatus": 1,
        "gameStatusText": "PPD",
        "period": 0,
        "gameClock": "",
        "gameTimeUTC": "2021-02-21T01:00:00Z",
        "gameEt": "2021-02-20T20:00:00Z",
        "regulationPeriods": 4,
        "seriesGameNumber": "",
        "seriesText": "",
        "homeTeam": {
          "teamId": 1610612745,
          "teamName": "Rockets",
          "teamCity": "Houston",
          "teamTricode": "HOU",
          "wins": 11,
          "losses": 17,
          "score": 0,
          "timeoutsRemaining": 0,
          "periods": [
            {
              "period": 1,
              "periodType": "REGULAR",
              "score": 0
            },
            {
              "period": 2,
              "periodType": "REGULAR",
              "score": 0
            },
            {
              "period": 3,
              "periodType": "REGULAR",
              "score": 0
            },
            {
              "period": 4,
              "periodType": "REGULAR",
              "score": 0
            }
          ]
        },
        "awayTeam": {
          "teamId": 1610612754,
          "teamName": "Pacers",
          "teamCity": "Indiana",
          "teamTricode": "IND",
          "wins": 15,
          "losses": 14,
          "score": 0,
          "timeoutsRemaining": 0,
          "periods": [
            {
              "period": 1,
              "periodType": "REGULAR",
              "score": 0
            },
            {
              "period": 2,
              "periodType": "REGULAR",
              "score": 0
            },
            {
              "period": 3,
              "periodType": "REGULAR",
              "score": 0
            },
            {
              "period": 4,
              "periodType": "REGULAR",
              "score": 0
            }
          ]
        },
        "gameLeaders": {
          "homeLeaders": {
            "personId": 0,
            "name": "",
            "jerseyNum": "",
            "position": "",
            "teamTricode": "HOU",
            "points": 0,
            "rebounds": 0,
            "assists": 0
          },
          "awayLeaders": {
            "personId": 0,
            "name": "",
            "jerseyNum": "",
            "position": "",
            "teamTricode": "IND",
            "points": 0,
            "rebounds": 0,
            "assists": 0
          }
        },
        "pbOdds": {
          "odds": 0.0,
          "suspended": 1
        }
      },
      {
        "gameId": "0022000463",
        "gameCode": "20210220/MIALAL",
        "gameStatus": 3,
        "gameStatusText": "Final",
        "period": 4,
        "gameClock": "",
        "gameTimeUTC": "2021-02-21T01:30:00Z",
        "gameEt": "2021-02-20T20:30:00Z",
        "regulationPeriods": 4,
        "seriesGameNumber": "",
        "seriesText": "",
        "homeTeam": {
          "teamId": 1610612747,
          "teamName": "Lakers",
          "teamCity": "Los Angeles",
          "teamTricode": "LAL",
          "wins": 22,
          "losses": 9,
          "score": 94,
          "timeoutsRemaining": 0,
          "periods": [
            {
              "period": 1,
              "periodType": "REGULAR",
              "score": 23
            },
            {
              "period": 2,
              "periodType": "REGULAR",
              "score": 29
            },
            {
              "period": 3,
              "periodType": "REGULAR",
              "score": 25
            },
            {
              "period": 4,
              "periodType": "REGULAR",
              "score": 17
            }
          ]
        },
        "awayTeam": {
          "teamId": 1610612748,
          "teamName": "Heat",
          "teamCity": "Miami",
          "teamTricode": "MIA",
          "wins": 13,
          "losses": 17,
          "score": 96,
          "timeoutsRemaining": 0,
          "periods": [
            {
              "period": 1,
              "periodType": "REGULAR",
              "score": 36
            },
            {
              "period": 2,
              "periodType": "REGULAR",
              "score": 23
            },
            {
              "period": 3,
              "periodType": "REGULAR",
              "score": 22
            },
            {
              "period": 4,
              "periodType": "REGULAR",
              "score": 15
            }
          ]
        },
        "gameLeaders": {
          "homeLeaders": {
            "personId": 2544,
            "name": "LeBron James",
            "jerseyNum": "23",
            "position": "F",
            "teamTricode": "LAL",
            "points": 19,
            "rebounds": 9,
            "assists": 9
          },
          "awayLeaders": {
            "personId": 202710,
            "name": "Jimmy Butler",
            "jerseyNum": "22",
            "position": "F",
            "teamTricode": "MIA",
            "points": 24,
            "rebounds": 8,
            "assists": 5
          }
        },
        "pbOdds": {
          "odds": 0.0,
          "suspended": 1
        }
      },
      {
        "gameId": "0022000460",
        "gameCode": "20210220/SACCHI",
        "gameStatus": 3,
        "gameStatusText": "Final",
        "period": 4,
        "gameClock": "",
        "gameTimeUTC": "2021-02-21T02:00:00Z",
        "gameEt": "2021-02-20T21:00:00Z",
        "regulationPeriods": 4,
        "seriesGameNumber": "",
        "seriesText": "",
        "homeTeam": {
          "teamId": 1610612741,
          "teamName": "Bulls",
          "teamCity": "Chicago",
          "teamTricode": "CHI",
          "wins": 13,
          "losses": 16,
          "score": 122,
          "timeoutsRemaining": 0,
          "periods": [
            {
              "period": 1,
              "periodType": "REGULAR",
              "score": 28
            },
            {
              "period": 2,
              "periodType": "REGULAR",
              "score": 40
            },
            {
              "period": 3,
              "periodType": "REGULAR",
              "score": 27
            },
            {
              "period": 4,
              "periodType": "REGULAR",
              "score": 27
            }
          ]
        },
        "awayTeam": {
          "teamId": 1610612758,
          "teamName": "Kings",
          "teamCity": "Sacramento",
          "teamTricode": "SAC",
          "wins": 12,
          "losses": 17,
          "score": 114,
          "timeoutsRemaining": 0,
          "periods": [
            {
              "period": 1,
              "periodType": "REGULAR",
              "score": 21
            },
            {
              "period": 2,
              "periodType": "REGULAR",
              "score": 37
            },
            {
              "period": 3,
              "periodType": "REGULAR",
              "score": 25
            },
            {
              "period": 4,
              "periodType": "REGULAR",
              "score": 31
            }
          ]
        },
        "gameLeaders": {
          "homeLeaders": {
            "personId": 203897,
            "name": "Zach LaVine",
            "jerseyNum": "8",
            "position": "G-F",
            "teamTricode": "CHI",
            "points": 38,
            "rebounds": 4,
            "assists": 3
          },
          "awayLeaders": {
            "personId": 1628963,
            "name": "Marvin Bagley III",
            "jerseyNum": "35",
            "position": "F",
            "teamTricode": "SAC",
            "points": 26,
            "rebounds": 11,
            "assists": 2
          }
        },
        "pbOdds": {
          "odds": 0.0,
          "suspended": 1
        }
      },
      {
        "gameId": "0022000462",
        "gameCode": "20210220/PHXMEM",
        "gameStatus": 3,
        "gameStatusText": "Final",
        "period": 4,
        "gameClock": "",
        "gameTimeUTC": "2021-02-21T02:00:00Z",
        "gameEt": "2021-02-20T21:00:00Z",
        "regulationPeriods": 4,
        "seriesGameNumber": "",
        "seriesText": "",
        "homeTeam": {
          "teamId": 1610612763,
          "teamName": "Grizzlies",
          "teamCity": "Memphis",
          "teamTricode": "MEM",
          "wins": 13,
          "losses": 13,
          "score": 97,
          "timeoutsRemaining": 0,
          "periods": [
            {
              "period": 1,
              "periodType": "REGULAR",
              "score": 15
            },
            {
              "period": 2,
              "periodType": "REGULAR",
              "score": 19
            },
            {
              "period": 3,
              "periodType": "REGULAR",
              "score": 30
            },
            {
              "period": 4,
              "periodType": "REGULAR",
              "score": 33
            }
          ]
        },
        "awayTeam": {
          "teamId": 1610612756,
          "teamName": "Suns",
          "teamCity": "Phoenix",
          "teamTricode": "PHX",
          "wins": 19,
          "losses": 10,
          "score": 128,
          "timeoutsRemaining": 1,
          "periods": [
            {
              "period": 1,
              "periodType": "REGULAR",
              "score": 28
            },
            {
              "period": 2,
              "periodType": "REGULAR",
              "score": 37
            },
            {
              "period": 3,
              "periodType": "REGULAR",
              "score": 31
            },
            {
              "period": 4,
              "periodType": "REGULAR",
              "score": 32
            }
          ]
        },
        "gameLeaders": {
          "homeLeaders": {
            "personId": 202685,
            "name": "Jonas Valanciunas",
            "jerseyNum": "17",
            "position": "C",
            "teamTricode": "MEM",
            "points": 10,
            "rebounds": 12,
            "assists": 1
          },
          "awayLeaders": {
            "personId": 1626164,
            "name": "Devin Booker",
            "jerseyNum": "1",
            "position": "G",
            "teamTricode": "PHX",
            "points": 23,
            "rebounds": 5,
            "assists": 5
          }
        },
        "pbOdds": {
          "odds": 0.0,
          "suspended": 1
        }
      },
      {
        "gameId": "0022000464",
        "gameCode": "20210220/WASPOR",
        "gameStatus": 3,
        "gameStatusText": "Final",
        "period": 4,
        "gameClock": "",
        "gameTimeUTC": "2021-02-21T03:00:00Z",
        "gameEt": "2021-02-20T22:00:00Z",
        "regulationPeriods": 4,
        "seriesGameNumber": "",
        "seriesText": "",
        "homeTeam": {
          "teamId": 1610612757,
          "teamName": "Trail Blazers",
          "teamCity": "Portland",
          "teamTricode": "POR",
          "wins": 18,
          "losses": 11,
          "score": 111,
          "timeoutsRemaining": 0,
          "periods": [
            {
              "period": 1,
              "periodType": "REGULAR",
              "score": 43
            },
            {
              "period": 2,
              "periodType": "REGULAR",
              "score": 12
            },
            {
              "period": 3,
              "periodType": "REGULAR",
              "score": 37
            },
            {
              "period": 4,
              "periodType": "REGULAR",
              "score": 19
            }
          ]
        },
        "awayTeam": {
          "teamId": 1610612764,
          "teamName": "Wizards",
          "teamCity": "Washington",
          "teamTricode": "WAS",
          "wins": 10,
          "losses": 17,
          "score": 118,
          "timeoutsRemaining": 0,
          "periods": [
            {
              "period": 1,
              "periodType": "REGULAR",
              "score": 31
            },
            {
              "period": 2,
              "periodType": "REGULAR",
              "score": 30
            },
            {
              "period": 3,
              "periodType": "REGULAR",
              "score": 28
            },
            {
              "period": 4,
              "periodType": "REGULAR",
              "score": 29
            }
          ]
        },
        "gameLeaders": {
          "homeLeaders": {
            "personId": 203081,
            "name": "Damian Lillard",
            "jerseyNum": "0",
            "position": "G",
            "teamTricode": "POR",
            "points": 35,
            "rebounds": 6,
            "assists": 12
          },
          "awayLeaders": {
            "personId": 201566,
            "name": "Russell Westbrook",
            "jerseyNum": "4",
            "position": "G",
            "teamTricode": "WAS",
            "points": 27,
            "rebounds": 11,
            "assists": 13
          }
        },
        "pbOdds": {
          "odds": 0.0,
          "suspended": 1
        }
      }
    ]
  }
}
scoreboard = data_set["scoreboard"]
games = scoreboard["games"]
game_date = scoreboard["gameDate"]
json_list_home = []
json_list_away = []
list_graph_qhome = []
i = 0
list_team_names = []
list_team_points = []
list_team_ratings = []
list_team_data = []
leader_names = []
leader_points = []
print("SCOREBOARD: " + str(game_date))
print()
for x in range(len(games)):
    json_list_home.append(games[x]["homeTeam"]["teamTricode"])
    json_list_away.append(games[x]["awayTeam"]["teamTricode"])
    print(json_list_home[x] + " vs. " + json_list_away[x] + "\t\tScore: " +
          str(games[x]["homeTeam"]["score"]) + " - " +
          str(games[x]["awayTeam"]["score"]))
    team_one = games[x]["homeTeam"]
    team_one_code = team_one["teamTricode"]
    list_team_names.append(team_one_code)
    team_one_score = team_one["score"]
    team_one_leader = games[x]["gameLeaders"]["homeLeaders"]["name"]
    team_one_leader_points = games[x]["gameLeaders"]["homeLeaders"]["points"]
    leader_names.append(team_one_leader)
    leader_points.append(team_one_leader_points)
    list_team_points.append(team_one_score)
    list_team_data.append(x)

    team_two = games[x]["awayTeam"]
    team_two_code = team_two["teamTricode"]
    team_two_score = team_two["score"]
    team_two_leader = games[x]["gameLeaders"]["awayLeaders"]["name"]
    team_two_leader_points = games[x]["gameLeaders"]["awayLeaders"]["points"]
    leader_names.append(team_two_leader)
    leader_points.append(team_two_leader_points)
    list_team_points.append(team_two_score)
    list_team_names.append(team_two_code)
    list_team_data.append(x)
    if team_one_score != 0 and team_two_score != 0:
        team_one_rating = team_one_score / team_two_score
        list_team_ratings.append(team_one_rating)
        team_two_rating = team_two_score / team_one_score
        list_team_ratings.append(team_two_rating)

    if team_one_score == 0:
        list_team_ratings.append(0)
    if team_two_score == 0:
        list_team_ratings.append(0)
print()
print("BucketAnalytics offers a wide range of graphical data representations to maximize basketball efficiency. The Progressive Scoring graphic models trends in team scoring during the four quarters of each game. The Leading Scorers graphic compares the top scorers each night with one another. The BucketAnalytics Efficiency Rating graphic is our specialized model which analyzes the relative offensive and defensive performances of NBA teams each night.")
print()

def graph_displays():
  graph_selection = input("Would you like to see the Progressive Scoring graphic, the Leading Scorers graphic, or the BucketAnalytics Efficiency Rating graphic (enter P, L, or B): ")
  print()
  if graph_selection == "P":
    team_name = input("Enter an NBA team (example input: PHX): ")
    for i in range(len(list_team_names)):
      if list_team_names[i] == team_name:
        if i % 2 == 0:
          points_scored = [games[list_team_data[i]]["homeTeam"]["periods"][0]["score"], games[list_team_data[i]]["homeTeam"]["periods"][1]["score"], games[list_team_data[i]]["homeTeam"]["periods"][2]["score"], games[list_team_data[i]]["homeTeam"]["periods"][3]["score"]]
        else:
          points_scored = [games[list_team_data[i]]["awayTeam"]["periods"][0]["score"], games[list_team_data[i]]["awayTeam"]["periods"][1]["score"], games[list_team_data[i]]["awayTeam"]["periods"][2]["score"], games[list_team_data[i]]["awayTeam"]["periods"][3]["score"]]
    if points_scored != 0:   
      game_progress = [1,2,3,4]
      fig = plt.figure(figsize = (7, 4)) 

      # creating the bar plot 
      plt.bar(game_progress, points_scored, color ='maroon',  
            width = 0.75) 

      plt.xlabel("Game Progress (Quarter Number)") 
      plt.ylabel("Points Scored Per Quarter") 
      plt.title("Points Scored vs. Game Progress for " + team_name + " on " + game_date) 
      plt.show()
    else:
      
      print(team_name + " did not play today")
    repeat_function()

  if graph_selection == "L":
    fig = plt.figure(figsize=(10, 4))
    plt.bar(list_team_names, leader_points, color='green', width=0.75)

    plt.xlabel("Team Name")
    plt.ylabel("Points Scored")
    plt.title("Teams' Highest Scoring Players " + str(game_date))
    plt.show()
    repeat_function()

  if graph_selection == "B":
    
    fig = plt.figure(figsize=(7, 4))
    plt.bar(list_team_names, list_team_ratings, color='blue', width=0.75)

    plt.xlabel("Team Name")
    plt.ylabel("BucketAnalytics Efficiency Rating")
    plt.title("BucketAnalytics Efficiency Ratings for NBA Teams on " + str(game_date))
    plt.show()
    repeat_function()

  else:
    print("Please enter a valid number")
    repeat_function()

def repeat_function():
  repeat = input("Would you like to continue (Y/N): ")
  if repeat == "Y":
    graph_displays()

graph_displays()
# if json contains abbreviation, then say that the team played today and display the graph
#else say the team did not play today, and stats will be available next time the tea
