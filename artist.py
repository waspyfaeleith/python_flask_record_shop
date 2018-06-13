class Artist(object):

    def __init__(self, name, id = None):
        self.repo = ArtistRepository()
        self.id = id
        self.name = name

    def save(self):
        self.repo.save(self)

    def update(self):
        self.repo.update(self)

    def albums(self):
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


from artist_repository import ArtistRepository
from album_repository import AlbumRepository
