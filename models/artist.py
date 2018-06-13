import sys
sys.path.append("..")

class Artist(object):

    def __init__(self, name, id = None):
        self._repo = ArtistRepository()
        self._id = id
        self._name = name

    @property
    def name(self):
        return self._name

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @name.setter
    def name(self, value):
        self._name = value

    def save(self):
        self._repo.save(self)

    def update(self):
        self._repo.update(self)

    def albums(self):
        from repositories.album_repository import AlbumRepository
        repo = AlbumRepository()
        albums = repo.select_for_artist(self.id)
        return albums

    @classmethod
    def all(self):
        repo = ArtistRepository()
        artists = repo.select_all()
        return artists

    @classmethod
    def find(self,id):
        repo = ArtistRepository()
        artist = repo.select(id)
        return artist

    @classmethod
    def delete(self, id):
        repo = ArtistRepository()
        repo.delete(id)

from repositories.artist_repository import ArtistRepository
