# from artist import Artist
from sql_runner import SqlRunner

class AlbumRepository(object):

    def select_all(self):
        albums = []
        sql = "SELECT * FROM albums"
        results = SqlRunner.run(sql)
        for row in results:
            album = Album(row['title'], row['artist_id'], row['quantity'], row['id'])
            albums.append(album)
        return albums

    def select(self, id):
        album = None
        sql = "SELECT * FROM albums WHERE id = %s"
        results = SqlRunner.run(sql,(id,))
        row = results[0]
        album = Album(row['title'], row['artist_id'], row['quantity'], row['id'])
        return album

    def select_for_artist(self, id):
        albums = []
        sql = "SELECT * FROM albums where artist_id = %s"
        results = SqlRunner.run(sql,(id,))
        for row in results:
            album = Album(row['title'], row['artist_id'], row['quantity'], row['id'])
            albums.append(album)
        return albums

    def save(self, album):
        sql = "INSERT INTO albums (title, artist_id, quantity) VALUES (%s, %s, %s) RETURNING id"
        results = SqlRunner.run(sql, (album.title, album.artist_id, album.quantity))
        id = results[0]['id']
        album.id = id
        return album

    def update(self, album):
        sql = "UPDATE albums SET (title, artist_id, quantity) = (%s, %s, %s) WHERE id = %s"
        SqlRunner.run(sql,(album.title, album.artist_id, album.quantity, album.id))

    def delete(self, id):
        sql = "DELETE FROM albums WHERE id = %s"
        SqlRunner.run(sql,(id,)).count

from album import Album
