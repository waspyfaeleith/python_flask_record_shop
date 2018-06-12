import unittest
import sys
#sys.path.append('../models')
sys.path.insert(0, '../models/')
from artist import Artist

class TestArtist(unittest.TestCase):

    def test_artist_name_is_set(self):
        artist = Artist('AC/DC')
        self.assertEqual('AC/DC', artist.name)

if __name__ == '__main__':
    unittest.main()
