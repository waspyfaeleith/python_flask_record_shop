from album_repository import AlbumRepository
from album import Album
from artist_repository import ArtistRepository
from artist import Artist

def print_all(repo):
    albums = repo.select_all()
    print(albums)
    for album in albums:
        print_album(album)

def print_album(album):
    print ("ID: %d, Title: %s, Artist ID: %d, Quantity: %d" % (album.id, album.title, album.artist_id, album.quantity))

def main():
    albumRepo = AlbumRepository()
    artistRepo = ArtistRepository()

    artist = artistRepo.select(1)

    print_all(albumRepo)

    album = Album("Highway to Hell", artist.id, 5)
    album = albumRepo.save(album)

    print_all(albumRepo)

    albumToFind = albumRepo.select(album.id)
    print_album(albumToFind)

    album.title = "Powerage"
    albumRepo.update(album)
    print_album(album)

    album.quantity = 999
    albumRepo.update(album)
    print_album(album)

    artist = Artist("Iron Maiden")
    artistRepo.save(artist)

    album.title = "Number of the Beast"
    album.artist_id = artist.id
    albumRepo.update(album)
    print_album(album)

    print_all(albumRepo)

    albumRepo.delete(album.id)
    print_all(albumRepo)

if __name__ == "__main__":
    main()
