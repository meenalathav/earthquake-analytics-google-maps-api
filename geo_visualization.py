#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 29 17:00:08 2021

@author: Meena V
"""


import sqlite3
import codecs

howmany = int(input("How many to dump?"))

import os
os.getcwd()

conn = sqlite3.connect('./index.sqlite')
conn.text_factory = str  # forces DB to return TEXT column values as strings
cur = conn.cursor()

cur.execute('''SELECT magnitude, lat, long FROM Earthquakes ORDER BY magnitude DESC''')

fhand = codecs.open('./where.js', 'w', 'utf-8')
fhand.write("myData = [")
count = 0 
for row in cur:
    
    mag = row[0]
    lat = row[1]
    lng = row[2]
    
    print(mag, lat, lng)
    count = count + 1
    
    if count > 1: fhand.write(",")
    fhand.write("["+str(lat)+","+str(lng)+",'"+str(mag)+"']")
    
    if count == howmany: break

fhand.write("];")

fhand.close()

print(count, "records written to where.js")
print("Open where.html to view the data in a browser")

#cur.execute('''SELECT * FROM Earthquakes ORDER BY magnitude DESC''')
#cur.fetchmany(10)

cur.close()