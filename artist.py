

class Artist(object):

    def __init__(self, name, id = None):
        self.id = id
        self.name = name

    @classmethod
    def all(self):
        repo = ArtistRepository()
        artists = repo.select_all()
        return artists

    def save(self):
        repo = ArtistRepository()
        repo.save(self)

from artist_repository import ArtistRepository
