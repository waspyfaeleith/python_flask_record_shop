import sys
sys.path.append("..")

import unittest

from models.album import Album
from models.artist import Artist

class TestAlbum(unittest.TestCase):

    def test_album_title_is_set(self):
        acdc = Artist("AC/DC")
        album = Album("Back in Black", acdc, 10)
        self.assertEqual("Back in Black", album.title)

    def test_album_artist_is_set(self):
        acdc = Artist("AC/DC")
        album = Album("Back in Black", acdc, 10)
        self.assertEqual("AC/DC", album.artist().name)

    def test_album_quantity_is_set(self):
        acdc = Artist("AC/DC")
        album = Album("Back in Black", acdc, 10)
        self.assertEqual(10, album.quantity)

    def test_album_title_changed(self):
        acdc = Artist("AC/DC")
        album = Album("Back in Black", acdc, 10)
        album.title = "Highway to Hell"
        self.assertEqual("Highway to Hell", album.title)

    def test_album_artist_is_changed(self):
        acdc = Artist("AC/DC")
        iron_maiden = Artist("Iron Maiden")
        album = Album("Back in Black", acdc, 10)
        album.artist = iron_maiden
        self.assertEqual("Iron Maiden", album.artist().name)

    def test_album_quantity_is_changed(self):
        acdc = Artist("AC/DC")
        album = Album("Back in Black", acdc, 10)
        album.quantity = 9
        self.assertEqual(9, album.quantity)

    def test_album_quantity_is_high(self):
        acdc = Artist("AC/DC")
        album = Album("Back in Black", acdc, 10)
        self.assertEqual("high", album.stock_level())

    def test_album_quantity_is_medium(self):
        acdc = Artist("AC/DC")
        album = Album("Back in Black", acdc, 7)
        self.assertEqual("medium", album.stock_level())

    def test_album_quantity_is_low(self):
        acdc = Artist("AC/DC")
        album = Album("Back in Black", acdc, 4)
        self.assertEqual("low", album.stock_level())

if __name__ == '__main__':
    unittest.main()
