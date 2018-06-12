from artist_repository import ArtistRepository
from artist import Artist

def print_all(repo):
    artists = repo.select_all()
    print(artists)
    for artist in artists:
        print (artist.name)

def main():
    repo = ArtistRepository()
    # print_all(repo)

    artist = Artist("Iron Maiden")
    artist = repo.save(artist)
    print_all(repo)

    artist = Artist("Anthrax")
    artist = repo.save(artist)
    print_all(repo)


    artist = repo.select(1)
    print (artist.name)

    #artist = artists[1]
    artist = repo.select(2)
    print("(BEFORE)ID: %d Name: %s" % (artist.id, artist.name))
    artist.name = "Black Sabbath"
    repo.update(artist)
    artist = repo.select(3)
    print("(AFTER)ID: %d Name: %s" % (artist.id, artist.name))
    print_all(repo)

    print(repo.delete(artist.id))
    print_all(repo)

    # artist = repo.select("1; DELETE * FROM artists;")
    # print_all(repo)
if __name__ == "__main__":
    main()
