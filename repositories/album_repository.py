import sys
sys.path.append("..")

from db.sql_runner import SqlRunner
from repositories.artist_repository import ArtistRepository

artist_repository = ArtistRepository()

class AlbumRepository(object):

    def select_all(self):
        albums = []
        sql = "SELECT * FROM albums"
        results = SqlRunner.run(sql)
        for row in results:
            artist = artist_repository.select(row['artist_id'])
            album = Album(row['title'], artist, row['quantity'], row['id'])
            albums.append(album)
        return albums

    def select(self, id):
        album = None
        sql = "SELECT * FROM albums WHERE id = %s"
        results = SqlRunner.run(sql,(id,))
        row = results[0]
        artist = artist_repository.select(row['artist_id'])
        album = Album(row['title'], artist, row['quantity'], row['id'])
        return album

    def select_for_artist(self, id):
        artist = artist_repository.select(id)
        albums = []
        sql = "SELECT * FROM albums where artist_id = %s"
        results = SqlRunner.run(sql,(id,))
        for row in results:
            album = Album(row['title'], artist, row['quantity'], row['id'])
            albums.append(album)
        return albums

    def save(self, album):
        sql = "INSERT INTO albums (title, artist_id, quantity) VALUES (%s, %s, %s) RETURNING id"
        results = SqlRunner.run(sql, (album.title, album.artist.id, album.quantity))
        id = results[0]['id']
        album.id = id
        return album

    def update(self, album):
        sql = "UPDATE albums SET (title, artist_id, quantity) = (%s, %s, %s) WHERE id = %s"
        SqlRunner.run(sql,(album.title, album.artist.id, album.quantity, album.id))

    def delete(self, id):
        sql = "DELETE FROM albums WHERE id = %s"
        SqlRunner.run(sql,(id,)).count

from models.album import Album
