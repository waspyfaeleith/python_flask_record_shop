class Album(object):
    def __init__(self, title, artist_id, quantity, id = None):
        self.title = title
        self.artist_id = artist_id
        self.quantity = quantity
        self.id = id
        self.repo = AlbumRepository()

    def save(self):
        self.repo.save(self)

    def update(self):
        self.repo.update(self)

    def artist(self):
        repo = ArtistRepository()
        artist = repo.select(self.artist_id)
        return artist

    @classmethod
    def all(self):
        repo = AlbumRepository()
        albums = repo.select_all()
        return albums

    @classmethod
    def find(self,id):
        repo = AlbumRepository()
        album = repo.select(id)
        return album

    @classmethod
    def delete(self, id):
        repo = AlbumRepository()
        repo.delete(id)

from album_repository import AlbumRepository
from artist_repository import ArtistRepository