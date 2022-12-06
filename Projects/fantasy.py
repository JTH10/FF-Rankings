from cgitb import text
from operator import contains
from unittest import result
from bs4 import BeautifulSoup
import requests
import re

week = "13"
pos = ["QB", "WR", "RB", "TE", "K", "DEF"]
for position in pos:
    if position == "QB":
        player_name = ["Joe Burrow", "Deshaun Watson"]
    elif position == "WR":
        player_name = ["Courtland Sutton", "Amari Cooper", "Keenan Allen", "Chris Godwin", ]
    elif position == "RB":
        player_name = ["Joe Mixon","Alvin Kamara", "Miles Sanders", "Kenneth Walker III", "Latavius Murray"]
    elif position == "TE":
        player_name = ["George Kittle"]
    elif position == "K":
        player_name = ["Tyler Bass"]
    elif position == "DEF":
        player_name = ["Dallas Cowboys", "New England Patriots"]

    url = f"https://fantasy.nfl.com/research/rankings?leagueId=0&position={position}&statSeason=2022&statType=weekStats&week={week}"

    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")


    print()
    print('\033[1m' + '\033[4m' + f"NFL.com {position} week {week} rank" + '\033[0m')

    #Create a dictionary of players and rank to sort before printing.
    NFL_com = dict()

    #Loop through players for each position.
    for name in player_name:
        try:

            #Extract Player ID
            search_name = doc.find_all(text=name)
            prnt = search_name[0].parent  
            player_id = str(prnt).split("-")[1].split(" ")[0]

            #Find player rank.
            player_rank = doc.find(class_=f"player-{player_id}").td.string
            NFL_com[name] = int(player_rank)

        # If player is not found input rank as 1000. Update "1000" to "Not Ranked" later on when printing
        except (IndexError):
            NFL_com[name] = 1000
            continue

    #Re-organize the dictionary by ranking (best to worst).
    sort = sorted([(v,k) for k,v in NFL_com.items()])
    for v,k in sort:

        #Update "1000" to "Not Ranked". See "except (IndexError):" & print NFL_com Dictionary.
        if v == 1000:
            print(f"{k} = Not Ranked")
        else:
            print(f"{k} = {v}")

##############################################
#Roto Pat

    if position == "TE" or position == "K" or position == "DEF":
        Roto_position = "te-k-def"
    else:
        Roto_position = position   

    url =f"https://www.nbcsportsedge.com/article/nfl-rankings/week-{week}-fantasy-football-rankings-{Roto_position}"

    result = requests.get(url)
    doc = BeautifulSoup(result.content, "html.parser")

    print()
    print()
    print('\033[1m' + '\033[4m' + f"Roto Pat {position} week {week} rank" + '\033[0m')

    #Create a dictionary of players and rank to sort before printing.
    Roto_pat = dict()

    #Loop through players for each position.
    for name in player_name:
        try:
            #Find the tag with the players name in it.
            search_name = doc.find_all("td", text=name)

            #Find the parent tag with the weekly rank.
            prnt = search_name[0].parent

            #Find the tag with the player rank and strip away the rank.
            Roto_rank = prnt.find("strong").text
            Roto_pat[name] = int(Roto_rank)

        # If player is not found input rank as 1000. Update "1000" to "Not Ranked" later on when printing
        except (IndexError):
            Roto_pat[name] = 1000
            continue

    #Re-organize the dictionary by ranking (best to worst).
    sort = sorted([(v,k) for k,v in Roto_pat.items()])
    for v,k in sort:

        #Update "1000" to "Not Ranked". See "except (IndexError):" & print Roto_pat Dictionary. 
        if v == 1000:
            print(f"{k} = Not Ranked")
        else:
            print(f"{k} = {v}")
    print()        
    print("//////////////////////////////////////////////////////////////////////////////")
