import xml.etree.ElementTree as ET
from flask import Flask
import re
import sqlite3

# Parse XML document as tree and root
tree = ET.parse('PnP.xml')
root = tree.getroot()

characters = []

# Iterate through document, looking for character Ids
for i in root.iter(tag="{http://www.tei-c.org/ns/1.0}person"):

  # Extract ID attribute as part of list to avoid namespace issue
  ids = list(dict.values(i.attrib))[1]

  # Iterate through those Ids to find character name tags for role, forename, and surname
  for j in i.iter(tag="{http://www.tei-c.org/ns/1.0}persName"):
    role = ""
    forename = ""
    surname = ""
    for k in j.iter(tag="{http://www.tei-c.org/ns/1.0}roleName"):
      role = ''.join(k.itertext())
    for l in j.iter(tag="{http://www.tei-c.org/ns/1.0}forename"):
      forename = ''.join(l.itertext())
    for m in j.iter(tag="{http://www.tei-c.org/ns/1.0}surname"):
      surname = ''.join(m.itertext())

# Create name by combining role, forename, and surname
    name = (role + ' ' + forename + ' ' + surname).rstrip().lstrip()
    name = re.sub(' +', ' ', name)
    #print(ids, name)

  # Print character id and name
  characters.append((ids, name))

#print(characters)

# Create / access database for speeches
con = sqlite3.connect("speeches.db")

# Call database cursor to execute SQL statements
cur = con.cursor()

# Insert character values into database
cur.executemany("INSERT INTO characters VALUES(?, ?)", characters)

# Commit changes to database
con.commit()

# To check work in output text
#for row in cur.execute('SELECT * FROM characters'):
    #print(row)