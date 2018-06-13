import sys
sys.path.append("..")

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
        from repositories.artist_repository import ArtistRepository
        repo = ArtistRepository()
        artist = repo.select(self.artist_id)
        return artist

    def stock_level(self):
        if (self.quantity >= 10):
            return "high"
        elif (self.quantity < 5):
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
#from repositories.artist_repository import ArtistRepository
