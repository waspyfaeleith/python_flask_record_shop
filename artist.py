class Artist(object):
    def __init__(self, name):
        self.id = None
        self.name = name

    def __init__(self, name, id = None):
        self.id = id
        self.name = name
