import sys
sys.path.append("..")

class Album(object):
    def __init__(self, title, artist, quantity, id = None):
        self._title = title
        self._artist = artist
        self._quantity = quantity
        self._id = id

    @property
    def title(self):
        return self._title

    @property
    def id(self):
        return self._id

    @property
    def artist(self):
        return self._artist

    @property
    def quantity(self):
        return self._quantity

    @id.setter
    def id(self, value):
        self._id = value

    @title.setter
    def title(self, value):
        self._title = value

    @artist.setter
    def artist(self, value):
        self._artist = value

    @quantity.setter
    def quantity(self, value):
        self._quantity = value

    def stock_level(self):
        if (self._quantity >= 10):
            return "high"
        elif (self._quantity < 5):
            return "low"
        else:
            return "medium"
