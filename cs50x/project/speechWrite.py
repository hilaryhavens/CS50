import xml.etree.ElementTree as ET
from flask import Flask
import sqlite3

# Parse XML document as tree and root
tree = ET.parse('PnP.xml')
root = tree.getroot()

speeches = []

# Iterate through document, looking through instances of spoken language indicated by "ref"
for i in root.iter(tag="{http://www.tei-c.org/ns/1.0}ref"):

  # Iterate through those speeches to find who is speaking by printing the "who" attribute of the "said" tag
  for j in i.iter(tag="{http://www.tei-c.org/ns/1.0}said"):
    who = j.get('who')

  # Add inner text mentioned between ref tags to document
  innerText = ''.join(i.itertext())

  # Print speaker id and inner text
  speeches.append((who, innerText))

#print(speeches)

# Create / access database for speeches
con = sqlite3.connect("speeches.db")

# Call database cursor to execute SQL statements
cur = con.cursor()

# Insert character values into database
cur.executemany("INSERT INTO speeches VALUES(?, ?)", speeches)

# Commit changes to database
con.commit()

# To check work in output text
#for row in cur.execute('SELECT * FROM speeches'):
    #print(row)
