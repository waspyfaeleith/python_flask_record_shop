import psycopg2
import psycopg2.extras as ext
from artist import Artist

from sql_runner import SqlRunner

class ArtistRepository(object):

    def select_all(self):
        artists = []
        sql = "SELECT * FROM artists"
        results = SqlRunner.run(sql)
        for row in results:
            artist = Artist(row['name'], row['id'])
            artists.append(artist)
        return artists

    def select(self, id):
        artist = None
        sql = "SELECT * FROM artists WHERE id = %s"
        results = SqlRunner.run(sql,(id,))
        row = results[0]
        artist = Artist(row['name'], row['id'])
        return artist

    def save(self, artist):
        sql = "INSERT INTO artists (name) VALUES (%s) RETURNING id"
        results = SqlRunner.run(sql, (artist.name,))
        id = results[0]['id']
        artist.id = id
        return artist

    def update(self, artist):
        sql = "UPDATE artists SET (name) = (%s) WHERE id = %s"
        SqlRunner.run(sql,(artist.name, artist.id))

    def delete(self, id):
        sql = "DELETE FROM artists WHERE id = %s"
        SqlRunner.run(sql,(id,)).count
