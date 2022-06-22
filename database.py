import sqlite3

conn = sqlite3.connect('players.db')
c = conn.cursor()

#c.execute("""CREATE TABLE players (
#        name text,
#        score integer
#)""")

#c.execute("INSERT INTO players VALUES ('dawtul',3)")
#c.execute("SELECT * FROM players ORDER BY score DESC")

print(c.fetchone())

#conn.commit()