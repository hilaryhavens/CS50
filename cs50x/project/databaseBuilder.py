import sqlite3

# Create / access database for speeches
con = sqlite3.connect("speeches.db")

# Call database cursor to execute SQL statements
cur = con.cursor()

# Create table for speeches
cur.execute("CREATE TABLE speeches(charId varchar(100), text varchar(60000))")

# Create table for character Ids
cur.execute("CREATE TABLE characters(id varchar(100), name varchar(255), FOREIGN KEY (id) REFERENCES speeches(charId))")
