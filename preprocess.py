# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 14:16:47 2020

@author: DavidMOBrien
"""

import sqlite3

conn = sqlite3.connect('database.sqlite')
c = conn.cursor()

airlineNames = []

for company in c.execute("SELECT DISTINCT airline FROM Tweets"):
    airlineNames.append(company)


for airline in airlineNames:
    fileName = airline[0] + '_tweets.txt'
    
    with open( fileName, 'w', encoding="utf-8" ) as f:
        for row in c.execute("SELECT text FROM Tweets WHERE airline=?",airline):
            split = row[0].split(' ')
            toWrite = ""
            for item in split[1:]:
                toWrite += item + ' '
            f.write(toWrite)
            f.write('\n')

