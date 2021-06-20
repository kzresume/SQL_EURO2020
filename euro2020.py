# import of a single pandas module
from pandas import read_html as pd

country_list = ['Italy','Switzerland','Turkey','Wales',
                'Belgium','Denmark','Finland','Russia',
                'Austria','Netherlands','North_Macedonia',
                'Ukraine','Croatia','Czech_Republic',
                'England','Scotland','Poland','Slovakia',
                'Spain','Sweden','France','Germany',
                'Hungary','Portugal',]

link = 'https://en.wikipedia.org/wiki/UEFA_Euro_2020_squads#Outfield_players'

# create a file sql to write
f = open('soccer.sql','w+')
f.write('CREATE TABLE COUNTRY (ID INTEGER PRIMARY KEY AUTOINCREMENT , NAME VARCHAR(50));\n')

for i in country_list:
    f.write('INSERT INTO COUNTRY(NAME) VALUES(\'{}\');\n'.format(i))
       
for i in country_list:
    f.write('CREATE TABLE {} (NUMBER INTEGER ,POSITION VARCHAR(3),PLAYER VARCHAR(50),CAPS INT,GOALS INT, CLUB VARCHAR(70));\n'.format(i))

data = pd(link)

f.write('CREATE TABLE ALL_PLAYERS (ID INTEGER PRIMARY KEY AUTOINCREMENT,NUMBER INTEGER ,POSITION VARCHAR(3),PLAYER VARCHAR(50),CAPS INTEGER,GOALS INTEGER, CLUB VARCHAR(70),COUNTRY_ID INTEGER);\n')

# 24 teams and max 26 players in each team
for i in range(24):
    for j in range(26):
        try:
            player = data[i].loc[j]
            data_list = (player['No.'],player['Pos.'],player['Player'],player['Caps'],player['Goals'],player['Club'],i+1)
            f.write('INSERT INTO ALL_PLAYERS (NUMBER,POSITION,PLAYER,CAPS,GOALS,CLUB,COUNTRY_ID) VALUES{};\n'.format(data_list))
        except:
            pass
#close and save a file
f.close()
    