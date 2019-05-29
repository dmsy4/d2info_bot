# -*- coding: utf-8 -*-
import requests
import re
from bs4 import BeautifulSoup

def region_ladder(region):
    url = 'http://www.dota2.com/webapi/ILeaderboard/GetDivisionLeaderboard/v0001?division='+region

    page = requests.get(url).text

    count = 0

    players = []

    for m in re.finditer(r'"name":"[-\`\[\]\.\w+\\]+"', page):
        if count == 10:
            break
        else:
            name = str(page[m.start()+8:m.end()-1])
            x = name.encode()
            players.append(x.decode('unicode_escape'))
            count += 1
    myText = ''

    for i in range(10):
        myText = myText + (str(i+1) + '. ' + players[i] + '\n')
    players_reg = '\n' + myText
    return players_reg