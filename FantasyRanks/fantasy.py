from cgitb import text
from operator import contains
from unittest import result
from bs4 import BeautifulSoup
import requests
import re

week = "9"
pos = ["QB", "WR", "RB", "TE", "K", "DEF"]
for position in pos:
    if position == "QB":
        player_name = ["Joe Burrow", "Tom Brady"]
    elif position == "WR":
        player_name = ["Courtland Sutton", "Amari Cooper", "Keenan Allen", "Chris Godwin"]
    elif position == "RB":
        player_name = ["Joe Mixon","Alvin Kamara", "Miles Sanders", "James Conner", "Kenneth Walker III"]
    elif position == "TE":
        player_name = ["George Kittle"]
    elif position == "K":
        player_name = ["Tyler Bass"]
    elif position == "DEF":
        player_name = ["Dallas Cowboys", "Los Angeles Rams"]

    url = f"https://fantasy.nfl.com/research/rankings?leagueId=0&position={position}&statSeason=2022&statType=weekStats&week={week}"

    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")

    print()
    print(f"NFL.com {position} week {week} rank")
    print("--------------")
    NFL_com = dict()
    for name in player_name:
        try:

            #Extract Player ID
            search_name = doc.find_all(text=name)
            prnt = search_name[0].parent
            
            player_id = str(prnt).split("-")[1].split(" ")[0]

            #Find player rank.
            player_rank = doc.find(class_=f"player-{player_id}").td.string
            #rank = player.find(class_="editorDraftRankRank")
            #rank = str(player).split(">")[1].split("<")[0]
            NFL_com[name] = int(player_rank)
        # If player is not found input rank as 1000. Update "1000" to "Not Ranked" later on when printing
        except (IndexError):
            NFL_com[name] = 1000
            continue
    sort = sorted([(v,k) for k,v in NFL_com.items()])
    for v,k in sort:
        #Update "1000" to "Not Ranked". See "except (IndexError):"
        if v == 1000:
            print(f"{k} = Not Ranked")
        else:
            print(f"{k} = {v}")
