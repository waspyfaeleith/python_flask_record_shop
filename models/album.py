import sys
sys.path.append("..")

class Album(object):
    def __init__(self, title, artist_id, quantity, id = None):
        self._title = title
        self._artist_id = artist_id
        self._quantity = quantity
        self._id = id
        self._repo = AlbumRepository()

    @property
    def title(self):
        return self._title

    @property
    def id(self):
        return self._id

    @property
    def artist_id(self):
        return self._artist_id

    @property
    def quantity(self):
        return self._quantity

    @id.setter
    def id(self, value):
        self._id = value

    @title.setter
    def title(self, value):
        self._title = value

    @artist_id.setter
    def artist_id(self, value):
        self._artist_id = value

    @quantity.setter
    def quantity(self, value):
        self._quantity = value

    def save(self):
        self._repo.save(self)

    def update(self):
        self._repo.update(self)

    def artist(self):
        from repositories.artist_repository import ArtistRepository
        repo = ArtistRepository()
        artist = repo.select(self.artist_id)
        return artist

    def stock_level(self):
        if (self._quantity >= 10):
            return "high"
        elif (self._quantity < 5):
            return "low"
        else:
            return "medium"

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

from repositories.album_repository import AlbumRepository
