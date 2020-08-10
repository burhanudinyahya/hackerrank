# Question 1 - Get total goal of team in selected year
# Ex: Liverpol at 2012
# team1 Liverpol as 'tuan rumah'
# team2 Liverpol as 'tamu'

import requests

def getTotalGoals(team, year):
    goal = 0

    res = requests.get("https://jsonmock.hackerrank.com/api/football_matches?year={}&team1={}&page=1".format(year, team))
    res = res.json()
    total_pages = res['total_pages']

    for i in range(1, total_pages+1):
        res = requests.get("https://jsonmock.hackerrank.com/api/football_matches?year={}&team1={}&page={}".format(year, team, i))
        res = res.json()

        for j in res['data']:
            goal += int(j['team1goals'])

    res = requests.get("https://jsonmock.hackerrank.com/api/football_matches?year={}&team2={}&page=1".format(year, team))
    res = res.json()
    total_pages = res['total_pages']

    for k in range(1, total_pages+1):
        res = requests.get("https://jsonmock.hackerrank.com/api/football_matches?year={}&team2={}&page={}".format(year, team, k))
        res = res.json()

        for l in res['data']:
            goal += int(l['team2goals'])


    return goal

# Question 2 - Get total goal of winner team in the competition by selected year
# Ex: Liga Ingris at 2012
# team1 Liverpol as 'tuan rumah'
# team2 Liverpol as 'tamu'


import requests

def getWinnerTotalGoals(competition, year):
    goal = 0

    res = requests.get("https://jsonmock.hackerrank.com/api/football_competitions?name={}&year={}".format(competition, year))
    res = res.json()
    winner = res['data'][0]['winner']

    res = requests.get("https://jsonmock.hackerrank.com/api/football_matches?competition={}&year={}&team1={}&page=1".format(competition, year, winner))
    res = res.json()
    total_pages = res['total_pages']

    for i in range(1, total_pages+1):
        res = requests.get("https://jsonmock.hackerrank.com/api/football_matches?competition={}&year={}&team1={}&page={}".format(competition, year, winner, i))
        res = res.json()
        print(res['data'])

        for j in res['data']:
            goal += int(j['team1goals'])

    res = requests.get("https://jsonmock.hackerrank.com/api/football_matches?competition={}&year={}&team2={}&page=1".format(competition, year, winner))
    res = res.json()
    total_pages = res['total_pages']

    for k in range(1, total_pages+1):
        res = requests.get("https://jsonmock.hackerrank.com/api/football_matches?competition={}&year={}&team2={}&page={}".format(competition, year, winner, k))
        res = res.json()
        print(res['data'])

        for l in res['data']:
            goal += int(l['team2goals'])

    return goal