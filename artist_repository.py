import psycopg2
import psycopg2.extras as ext
from artist import Artist
from sql_runner import SqlRunner

class ArtistRepository(object):
    # def __init__(self):
    #     self.db = 'record_store'
    #     self.table = 'artists'

    # def db_connect(self):
    #     conn = None
    #     try:
    #         conn=psycopg2.connect("dbname='record_store'")
    #     except (Exception, psycopg2.DatabaseError) as error:
    #         print(error)
    #     return conn


    def select_all(self):
        artists = []
        # conn = None
        sql = "SELECT * FROM artists"
        # try:
        #     conn = self.db_connect()
        #     cur = conn.cursor(cursor_factory=ext.DictCursor)
        #     cur.execute(sql)
        #     rows = cur.fetchall()
        #     for row in rows:
        #         artist = Artist(row['name'], row['id'])
        #         results.append(artist)
        #     cur.close()
        # except (Exception, psycopg2.DatabaseError) as error:
        #     print(error)
        # finally:
        #     if conn is not None:
        #         conn.close()
        results = SqlRunner.run(sql)
        for row in results:
            artist = Artist(row['name'], row['id'])
            artists.append(artist)
        return artists

    def select(self, id):
        artist = None
        #conn = None
        sql = "SELECT * FROM artists WHERE id = %s"
        results = SqlRunner.run(sql,(id,))
        row = results[0]
        artist = Artist(row['name'], row['id'])
        return artist

        # try:
        #     conn = self.db_connect()
        #     cur = conn.cursor(cursor_factory=ext.DictCursor)
        #     cur.execute(sql, (id,))
        #     rows = cur.fetchall()
        #     result = rows[0]
        #     artist = Artist(result['name'], result['id'])
        #     cur.close()
        # except (Exception, psycopg2.DatabaseError) as error:
        #     print(error)
        # finally:
        #     if conn is not None:
        #         conn.close()

        #return artist


    def save(self, artist):
        conn = None
        sql = "INSERT INTO artists (name) VALUES (%s) RETURNING id"
        results = SqlRunner.run(sql, (artist.name,))
        id = results[0]['id']
        artist.id = id
        return artist
        # sql = "INSERT INTO artists (name) VALUES (%s) RETURNING id"
        # try:
        #     conn = self.db_connect()
        #     cur = conn.cursor()
        #     cur.execute(sql, (artist.name,))
        #     id = cur.fetchone()[0]
        #     conn.commit()
        #     cur.close()
        #     artist.id = id
        # except (Exception, psycopg2.DatabaseError) as error:
        #     print(error)
        # finally:
        #     if conn is not None:
        #         conn.close()
        # return artist

    def update(self, artist):
        # updated_rows = 0
        # sql = "UPDATE artists SET (name) = (%s) WHERE id = %s"
        # conn = None
        updated_rows = 0
        print("ID: %d Changing to Name: %s" % (artist.id, artist.name))
        sql = "UPDATE artists SET (name) = (%s) WHERE id = %s"
        SqlRunner.run(sql,(artist.name, artist.id))
        # try:
        #     conn = self.db_connect()
        #     cur = conn.cursor()
        #     cur.execute(sql,(artist.name, artist.id))
        #     updated_rows = cur.rowcount
        #     conn.commit()
        #     cur.close()
        # except (Exception, psycopg2.DatabaseError) as error:
        #     print(error)
        # finally:
        #     if conn is not None:
        #         conn.close()

    def delete(self, id):
        #conn = None
        rows_deleted = 0
        sql = "DELETE FROM artists WHERE id = %s"
        # try:
        #     conn = self.db_connect()
        #     cur = conn.cursor()
        #     cur.execute(sql, (id,))
        #     rows_deleted = cur.rowcount
        #     conn.commit()
        #     cur.close()
        # except (Exception, psycopg2.DatabaseError) as error:
        #     print(error)
        # finally:
        #     if conn is not None:
        #         conn.close()
        rows_deleted = SqlRunner.run(sql,(id,)).count
        return rows_deleted
