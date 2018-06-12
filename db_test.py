import psycopg2
import psycopg2.extras
from artist import Artist

# Try to connect

try:
    conn=psycopg2.connect("dbname='record_store'")
except:
    print("I am unable to connect to the database.")

#cur = conn.cursor()
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
try:
    cur.execute("""INSERT INTO artists(name) VALUES('Iron Maiden')""")
except:
    print("I can't INSERT into artists")

try:
    cur.execute("""SELECT * from artists""")
except:
    print("I can't SELECT from artists")

rows = cur.fetchall()
results = []
for row in rows:
    artist = Artist(row['name'])
    results.append(artist)

for result in results:
    print(result.name)
